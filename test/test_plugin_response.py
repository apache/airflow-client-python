# coding: utf-8

"""
    Airflow API

    Airflow API. All endpoints located under ``/api/v2`` can be used safely, are stable and backward compatible. Endpoints located under ``/ui`` are dedicated to the UI and are subject to breaking change depending on the need of the frontend. Users should not rely on those but use the public ones instead.

    The version of the OpenAPI document: 2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from airflow_client.client.models.plugin_response import PluginResponse

class TestPluginResponse(unittest.TestCase):
    """PluginResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PluginResponse:
        """Test PluginResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PluginResponse`
        """
        model = PluginResponse()
        if include_optional:
            return PluginResponse(
                appbuilder_menu_items = [
                    airflow_client.client.models.app_builder_menu_item_response.AppBuilderMenuItemResponse(
                        category = '', 
                        href = '', 
                        name = '', )
                    ],
                appbuilder_views = [
                    airflow_client.client.models.app_builder_view_response.AppBuilderViewResponse(
                        category = '', 
                        label = '', 
                        name = '', 
                        view = '', )
                    ],
                fastapi_apps = [
                    airflow_client.client.models.fast_api_app_response.FastAPIAppResponse(
                        app = '', 
                        name = '', 
                        url_prefix = '', )
                    ],
                fastapi_root_middlewares = [
                    airflow_client.client.models.fast_api_root_middleware_response.FastAPIRootMiddlewareResponse(
                        middleware = '', 
                        name = '', )
                    ],
                flask_blueprints = [
                    ''
                    ],
                global_operator_extra_links = [
                    ''
                    ],
                listeners = [
                    ''
                    ],
                macros = [
                    ''
                    ],
                name = '',
                operator_extra_links = [
                    ''
                    ],
                source = '',
                timetables = [
                    ''
                    ]
            )
        else:
            return PluginResponse(
                appbuilder_menu_items = [
                    airflow_client.client.models.app_builder_menu_item_response.AppBuilderMenuItemResponse(
                        category = '', 
                        href = '', 
                        name = '', )
                    ],
                appbuilder_views = [
                    airflow_client.client.models.app_builder_view_response.AppBuilderViewResponse(
                        category = '', 
                        label = '', 
                        name = '', 
                        view = '', )
                    ],
                fastapi_apps = [
                    airflow_client.client.models.fast_api_app_response.FastAPIAppResponse(
                        app = '', 
                        name = '', 
                        url_prefix = '', )
                    ],
                fastapi_root_middlewares = [
                    airflow_client.client.models.fast_api_root_middleware_response.FastAPIRootMiddlewareResponse(
                        middleware = '', 
                        name = '', )
                    ],
                flask_blueprints = [
                    ''
                    ],
                global_operator_extra_links = [
                    ''
                    ],
                listeners = [
                    ''
                    ],
                macros = [
                    ''
                    ],
                name = '',
                operator_extra_links = [
                    ''
                    ],
                source = '',
                timetables = [
                    ''
                    ],
        )
        """

    def testPluginResponse(self):
        """Test PluginResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
