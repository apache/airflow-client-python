# coding: utf-8

"""
    Airflow API

    Airflow API. All endpoints located under ``/api/v2`` can be used safely, are stable and backward compatible. Endpoints located under ``/ui`` are dedicated to the UI and are subject to breaking change depending on the need of the frontend. Users should not rely on those but use the public ones instead.

    The version of the OpenAPI document: 2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from airflow_client.client.api.backfill_api import BackfillApi


class TestBackfillApi(unittest.TestCase):
    """BackfillApi unit test stubs"""

    def setUp(self) -> None:
        self.api = BackfillApi()

    def tearDown(self) -> None:
        pass

    def test_cancel_backfill(self) -> None:
        """Test case for cancel_backfill

        Cancel Backfill
        """
        pass

    def test_create_backfill(self) -> None:
        """Test case for create_backfill

        Create Backfill
        """
        pass

    def test_create_backfill_dry_run(self) -> None:
        """Test case for create_backfill_dry_run

        Create Backfill Dry Run
        """
        pass

    def test_get_backfill(self) -> None:
        """Test case for get_backfill

        Get Backfill
        """
        pass

    def test_list_backfills(self) -> None:
        """Test case for list_backfills

        List Backfills
        """
        pass

    def test_pause_backfill(self) -> None:
        """Test case for pause_backfill

        Pause Backfill
        """
        pass

    def test_unpause_backfill(self) -> None:
        """Test case for unpause_backfill

        Unpause Backfill
        """
        pass


if __name__ == '__main__':
    unittest.main()
