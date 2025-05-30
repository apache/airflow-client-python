# coding: utf-8

"""
    Airflow API

    Airflow API. All endpoints located under ``/api/v2`` can be used safely, are stable and backward compatible. Endpoints located under ``/ui`` are dedicated to the UI and are subject to breaking change depending on the need of the frontend. Users should not rely on those but use the public ones instead.

    The version of the OpenAPI document: 2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from airflow_client.client.models.task_instance_history_response import TaskInstanceHistoryResponse

class TestTaskInstanceHistoryResponse(unittest.TestCase):
    """TaskInstanceHistoryResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TaskInstanceHistoryResponse:
        """Test TaskInstanceHistoryResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TaskInstanceHistoryResponse`
        """
        model = TaskInstanceHistoryResponse()
        if include_optional:
            return TaskInstanceHistoryResponse(
                dag_id = '',
                dag_run_id = '',
                dag_version = airflow_client.client.models.dag_version_response.DagVersionResponse(
                    bundle_name = '', 
                    bundle_url = '', 
                    bundle_version = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    dag_id = '', 
                    id = '', 
                    version_number = 56, ),
                duration = 1.337,
                end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                executor = '',
                executor_config = '',
                hostname = '',
                map_index = 56,
                max_tries = 56,
                operator = '',
                pid = 56,
                pool = '',
                pool_slots = 56,
                priority_weight = 56,
                queue = '',
                queued_when = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                scheduled_when = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                state = 'removed',
                task_display_name = '',
                task_id = '',
                try_number = 56,
                unixname = ''
            )
        else:
            return TaskInstanceHistoryResponse(
                dag_id = '',
                dag_run_id = '',
                executor_config = '',
                map_index = 56,
                max_tries = 56,
                pool = '',
                pool_slots = 56,
                task_display_name = '',
                task_id = '',
                try_number = 56,
        )
        """

    def testTaskInstanceHistoryResponse(self):
        """Test TaskInstanceHistoryResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
