import json
import logging

from airflow.models.baseoperator import BaseOperator

from dbt_airflow_manifest_parser.operator import DbtRunOperatorBuilder
from dbt_airflow_manifest_parser.tasks import ModelExecutionTask, ModelExecutionTasks


class DbtAirflowTasksBuilder:
    def __init__(self, operator_builder: DbtRunOperatorBuilder):
        self.operator_builder = operator_builder

    def _load_dbt_manifest(self, manifest_path: str) -> dict:
        with open(manifest_path, "r") as f:
            manifest_content = json.load(f)
            logging.debug("Manifest content: " + str(manifest_content))
            return manifest_content

    def _make_dbt_test_task(self, model_name: str) -> BaseOperator:
        return self.operator_builder.create(model_name + "_test", "test", model_name)

    def _make_dbt_run_task(self, model_name: str) -> BaseOperator:
        return self.operator_builder.create(model_name + "_run", "run", model_name)

    @staticmethod
    def _is_model_run_task(node_name: str):
        return node_name.split(".")[0] == "model"

    def _create_tasks_for_each_model(self, manifest: dict) -> dict:
        tasks = {}
        for node_name in manifest["nodes"].keys():
            if self._is_model_run_task(node_name):
                logging.info("Creating tasks for: " + node_name)
                model_name = node_name.split(".")[-1]
                run_task = self._make_dbt_run_task(model_name)
                test_task = self._make_dbt_test_task(model_name)
                # noinspection PyStatementEffect
                run_task >> test_task
                tasks[node_name] = ModelExecutionTask(run_task, test_task)
        return tasks

    def _create_tasks_dependencies(
        self, manifest: dict, tasks: dict
    ) -> ModelExecutionTasks:
        starting_tasks = list(tasks.keys())
        ending_tasks = list(tasks.keys())
        for node_name in tasks.keys():
            for upstream_node in manifest["nodes"][node_name]["depends_on"]["nodes"]:
                if self._is_model_run_task(upstream_node):
                    # noinspection PyStatementEffect
                    (
                        tasks[upstream_node].test_airflow_task
                        >> tasks[node_name].run_airflow_task
                    )
                    if node_name in starting_tasks:
                        starting_tasks.remove(node_name)
                    if upstream_node in ending_tasks:
                        ending_tasks.remove(upstream_node)
        return ModelExecutionTasks(tasks, starting_tasks, ending_tasks)

    def _make_dbt_tasks(self, manifest_path: str) -> ModelExecutionTasks:
        manifest = self._load_dbt_manifest(manifest_path)
        tasks = self._create_tasks_for_each_model(manifest)
        tasks_with_context = self._create_tasks_dependencies(manifest, tasks)
        logging.info(f"Created {str(tasks_with_context.length())} tasks groups")
        return tasks_with_context

    def parse_manifest_into_tasks(self, manifest_path) -> ModelExecutionTasks:
        return self._make_dbt_tasks(manifest_path)

    def create_seed_task(self) -> BaseOperator:
        return self.operator_builder.create("dbt_seed", "seed")
