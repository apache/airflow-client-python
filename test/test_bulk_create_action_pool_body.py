# coding: utf-8

"""
    Airflow API

    Airflow API. All endpoints located under ``/api/v2`` can be used safely, are stable and backward compatible. Endpoints located under ``/ui`` are dedicated to the UI and are subject to breaking change depending on the need of the frontend. Users should not rely on those but use the public ones instead.

    The version of the OpenAPI document: 2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from airflow_client.client.models.bulk_create_action_pool_body import BulkCreateActionPoolBody

class TestBulkCreateActionPoolBody(unittest.TestCase):
    """BulkCreateActionPoolBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BulkCreateActionPoolBody:
        """Test BulkCreateActionPoolBody
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BulkCreateActionPoolBody`
        """
        model = BulkCreateActionPoolBody()
        if include_optional:
            return BulkCreateActionPoolBody(
                action = 'create',
                action_on_existence = 'fail',
                entities = [
                    airflow_client.client.models.pool_body.PoolBody(
                        description = '', 
                        include_deferred = True, 
                        name = '', 
                        slots = 56, )
                    ]
            )
        else:
            return BulkCreateActionPoolBody(
                action = 'create',
                entities = [
                    airflow_client.client.models.pool_body.PoolBody(
                        description = '', 
                        include_deferred = True, 
                        name = '', 
                        slots = 56, )
                    ],
        )
        """

    def testBulkCreateActionPoolBody(self):
        """Test BulkCreateActionPoolBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
