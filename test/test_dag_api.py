# coding: utf-8

"""
    Airflow API

    Airflow API. All endpoints located under ``/api/v2`` can be used safely, are stable and backward compatible. Endpoints located under ``/ui`` are dedicated to the UI and are subject to breaking change depending on the need of the frontend. Users should not rely on those but use the public ones instead.

    The version of the OpenAPI document: 2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from airflow_client.client.api.dag_api import DAGApi


class TestDAGApi(unittest.TestCase):
    """DAGApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DAGApi()

    def tearDown(self) -> None:
        pass

    def test_delete_dag(self) -> None:
        """Test case for delete_dag

        Delete Dag
        """
        pass

    def test_get_dag(self) -> None:
        """Test case for get_dag

        Get Dag
        """
        pass

    def test_get_dag_details(self) -> None:
        """Test case for get_dag_details

        Get Dag Details
        """
        pass

    def test_get_dag_tags(self) -> None:
        """Test case for get_dag_tags

        Get Dag Tags
        """
        pass

    def test_get_dags(self) -> None:
        """Test case for get_dags

        Get Dags
        """
        pass

    def test_patch_dag(self) -> None:
        """Test case for patch_dag

        Patch Dag
        """
        pass

    def test_patch_dags(self) -> None:
        """Test case for patch_dags

        Patch Dags
        """
        pass


if __name__ == '__main__':
    unittest.main()
