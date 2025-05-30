# coding: utf-8

"""
    Airflow API

    Airflow API. All endpoints located under ``/api/v2`` can be used safely, are stable and backward compatible. Endpoints located under ``/ui`` are dedicated to the UI and are subject to breaking change depending on the need of the frontend. Users should not rely on those but use the public ones instead.

    The version of the OpenAPI document: 2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from airflow_client.client.models.dag_collection_response import DAGCollectionResponse

class TestDAGCollectionResponse(unittest.TestCase):
    """DAGCollectionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DAGCollectionResponse:
        """Test DAGCollectionResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DAGCollectionResponse`
        """
        model = DAGCollectionResponse()
        if include_optional:
            return DAGCollectionResponse(
                dags = [
                    airflow_client.client.models.dag_response.DAGResponse(
                        bundle_name = '', 
                        bundle_version = '', 
                        dag_display_name = '', 
                        dag_id = '', 
                        description = '', 
                        file_token = '', 
                        fileloc = '', 
                        has_import_errors = True, 
                        has_task_concurrency_limits = True, 
                        is_paused = True, 
                        is_stale = True, 
                        last_expired = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_parsed_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        max_active_runs = 56, 
                        max_active_tasks = 56, 
                        max_consecutive_failed_dag_runs = 56, 
                        next_dagrun_data_interval_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        next_dagrun_data_interval_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        next_dagrun_logical_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        next_dagrun_run_after = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        owners = [
                            ''
                            ], 
                        relative_fileloc = '', 
                        tags = [
                            airflow_client.client.models.dag_tag_response.DagTagResponse(
                                dag_id = '', 
                                name = '', )
                            ], 
                        timetable_description = '', 
                        timetable_summary = '', )
                    ],
                total_entries = 56
            )
        else:
            return DAGCollectionResponse(
                dags = [
                    airflow_client.client.models.dag_response.DAGResponse(
                        bundle_name = '', 
                        bundle_version = '', 
                        dag_display_name = '', 
                        dag_id = '', 
                        description = '', 
                        file_token = '', 
                        fileloc = '', 
                        has_import_errors = True, 
                        has_task_concurrency_limits = True, 
                        is_paused = True, 
                        is_stale = True, 
                        last_expired = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_parsed_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        max_active_runs = 56, 
                        max_active_tasks = 56, 
                        max_consecutive_failed_dag_runs = 56, 
                        next_dagrun_data_interval_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        next_dagrun_data_interval_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        next_dagrun_logical_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        next_dagrun_run_after = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        owners = [
                            ''
                            ], 
                        relative_fileloc = '', 
                        tags = [
                            airflow_client.client.models.dag_tag_response.DagTagResponse(
                                dag_id = '', 
                                name = '', )
                            ], 
                        timetable_description = '', 
                        timetable_summary = '', )
                    ],
                total_entries = 56,
        )
        """

    def testDAGCollectionResponse(self):
        """Test DAGCollectionResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
