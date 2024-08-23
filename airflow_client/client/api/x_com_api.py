"""
    Airflow API (Stable)

    # Overview  To facilitate management, Apache Airflow supports a range of REST API endpoints across its objects. This section provides an overview of the API design, methods, and supported use cases.  Most of the endpoints accept `JSON` as input and return `JSON` responses. This means that you must usually add the following headers to your request: ``` Content-type: application/json Accept: application/json ```  ## Resources  The term `resource` refers to a single type of object in the Airflow metadata. An API is broken up by its endpoint's corresponding resource. The name of a resource is typically plural and expressed in camelCase. Example: `dagRuns`.  Resource names are used as part of endpoint URLs, as well as in API parameters and responses.  ## CRUD Operations  The platform supports **C**reate, **R**ead, **U**pdate, and **D**elete operations on most resources. You can review the standards for these operations and their standard parameters below.  Some endpoints have special behavior as exceptions.  ### Create  To create a resource, you typically submit an HTTP `POST` request with the resource's required metadata in the request body. The response returns a `201 Created` response code upon success with the resource's metadata, including its internal `id`, in the response body.  ### Read  The HTTP `GET` request can be used to read a resource or to list a number of resources.  A resource's `id` can be submitted in the request parameters to read a specific resource. The response usually returns a `200 OK` response code upon success, with the resource's metadata in the response body.  If a `GET` request does not include a specific resource `id`, it is treated as a list request. The response usually returns a `200 OK` response code upon success, with an object containing a list of resources' metadata in the response body.  When reading resources, some common query parameters are usually available. e.g.: ``` v1/connections?limit=25&offset=25 ```  |Query Parameter|Type|Description| |---------------|----|-----------| |limit|integer|Maximum number of objects to fetch. Usually 25 by default| |offset|integer|Offset after which to start returning objects. For use with limit query parameter.|  ### Update  Updating a resource requires the resource `id`, and is typically done using an HTTP `PATCH` request, with the fields to modify in the request body. The response usually returns a `200 OK` response code upon success, with information about the modified resource in the response body.  ### Delete  Deleting a resource requires the resource `id` and is typically executed via an HTTP `DELETE` request. The response usually returns a `204 No Content` response code upon success.  ## Conventions  - Resource names are plural and expressed in camelCase. - Names are consistent between URL parameter name and field name.  - Field names are in snake_case. ```json {     \"description\": \"string\",     \"name\": \"string\",     \"occupied_slots\": 0,     \"open_slots\": 0     \"queued_slots\": 0,     \"running_slots\": 0,     \"scheduled_slots\": 0,     \"slots\": 0, } ```  ### Update Mask  Update mask is available as a query parameter in patch endpoints. It is used to notify the API which fields you want to update. Using `update_mask` makes it easier to update objects by helping the server know which fields to update in an object instead of updating all fields. The update request ignores any fields that aren't specified in the field mask, leaving them with their current values.  Example: ```   resource = request.get('/resource/my-id').json()   resource['my_field'] = 'new-value'   request.patch('/resource/my-id?update_mask=my_field', data=json.dumps(resource)) ```  ## Versioning and Endpoint Lifecycle  - API versioning is not synchronized to specific releases of the Apache Airflow. - APIs are designed to be backward compatible. - Any changes to the API will first go through a deprecation phase.  # Trying the API  You can use a third party client, such as [curl](https://curl.haxx.se/), [HTTPie](https://httpie.org/), [Postman](https://www.postman.com/) or [the Insomnia rest client](https://insomnia.rest/) to test the Apache Airflow API.  Note that you will need to pass credentials data.  For e.g., here is how to pause a DAG with [curl](https://curl.haxx.se/), when basic authorization is used: ```bash curl -X PATCH 'https://example.com/api/v1/dags/{dag_id}?update_mask=is_paused' \\ -H 'Content-Type: application/json' \\ --user \"username:password\" \\ -d '{     \"is_paused\": true }' ```  Using a graphical tool such as [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/), it is possible to import the API specifications directly:  1. Download the API specification by clicking the **Download** button at the top of this document 2. Import the JSON specification in the graphical tool of your choice.   - In *Postman*, you can click the **import** button at the top   - With *Insomnia*, you can just drag-and-drop the file on the UI  Note that with *Postman*, you can also generate code snippets by selecting a request and clicking on the **Code** button.  ## Enabling CORS  [Cross-origin resource sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) is a browser security feature that restricts HTTP requests that are initiated from scripts running in the browser.  For details on enabling/configuring CORS, see [Enabling CORS](https://airflow.apache.org/docs/apache-airflow/stable/security/api.html).  # Authentication  To be able to meet the requirements of many organizations, Airflow supports many authentication methods, and it is even possible to add your own method.  If you want to check which auth backend is currently set, you can use `airflow config get-value api auth_backends` command as in the example below. ```bash $ airflow config get-value api auth_backends airflow.api.auth.backend.basic_auth ``` The default is to deny all requests.  For details on configuring the authentication, see [API Authorization](https://airflow.apache.org/docs/apache-airflow/stable/security/api.html).  # Errors  We follow the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs. As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.  ## Unauthenticated  This indicates that the request has not been applied because it lacks valid authentication credentials for the target resource. Please check that you have valid credentials.  ## PermissionDenied  This response means that the server understood the request but refuses to authorize it because it lacks sufficient rights to the resource. It happens when you do not have the necessary permission to execute the action you performed. You need to get the appropriate permissions in other to resolve this error.  ## BadRequest  This response means that the server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). To resolve this, please ensure that your syntax is correct.  ## NotFound  This client error response indicates that the server cannot find the requested resource.  ## MethodNotAllowed  Indicates that the request method is known by the server but is not supported by the target resource.  ## NotAcceptable  The target resource does not have a current representation that would be acceptable to the user agent, according to the proactive negotiation header fields received in the request, and the server is unwilling to supply a default representation.  ## AlreadyExists  The request could not be completed due to a conflict with the current state of the target resource, e.g. the resource it tries to create already exists.  ## Unknown  This means that the server encountered an unexpected condition that prevented it from fulfilling the request.   # noqa: E501

    The version of the OpenAPI document: 2.10.0
    Contact: dev@airflow.apache.org
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from airflow_client.client.api_client import ApiClient, Endpoint as _Endpoint
from airflow_client.client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from airflow_client.client.model.error import Error
from airflow_client.client.model.x_com import XCom
from airflow_client.client.model.x_com_collection import XComCollection


class XComApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_xcom_entries_endpoint = _Endpoint(
            settings={
                'response_type': (XComCollection,),
                'auth': [
                    'Basic',
                    'Kerberos'
                ],
                'endpoint_path': '/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/xcomEntries',
                'operation_id': 'get_xcom_entries',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'dag_id',
                    'dag_run_id',
                    'task_id',
                    'map_index',
                    'xcom_key',
                    'limit',
                    'offset',
                ],
                'required': [
                    'dag_id',
                    'dag_run_id',
                    'task_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'offset',
                ]
            },
            root_map={
                'validations': {
                    ('offset',): {

                        'inclusive_minimum': 0,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'dag_id':
                        (str,),
                    'dag_run_id':
                        (str,),
                    'task_id':
                        (str,),
                    'map_index':
                        (int,),
                    'xcom_key':
                        (str,),
                    'limit':
                        (int,),
                    'offset':
                        (int,),
                },
                'attribute_map': {
                    'dag_id': 'dag_id',
                    'dag_run_id': 'dag_run_id',
                    'task_id': 'task_id',
                    'map_index': 'map_index',
                    'xcom_key': 'xcom_key',
                    'limit': 'limit',
                    'offset': 'offset',
                },
                'location_map': {
                    'dag_id': 'path',
                    'dag_run_id': 'path',
                    'task_id': 'path',
                    'map_index': 'query',
                    'xcom_key': 'query',
                    'limit': 'query',
                    'offset': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_xcom_entry_endpoint = _Endpoint(
            settings={
                'response_type': (XCom,),
                'auth': [
                    'Basic',
                    'Kerberos'
                ],
                'endpoint_path': '/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/xcomEntries/{xcom_key}',
                'operation_id': 'get_xcom_entry',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'dag_id',
                    'dag_run_id',
                    'task_id',
                    'xcom_key',
                    'map_index',
                    'deserialize',
                    'stringify',
                ],
                'required': [
                    'dag_id',
                    'dag_run_id',
                    'task_id',
                    'xcom_key',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'dag_id':
                        (str,),
                    'dag_run_id':
                        (str,),
                    'task_id':
                        (str,),
                    'xcom_key':
                        (str,),
                    'map_index':
                        (int,),
                    'deserialize':
                        (bool,),
                    'stringify':
                        (bool,),
                },
                'attribute_map': {
                    'dag_id': 'dag_id',
                    'dag_run_id': 'dag_run_id',
                    'task_id': 'task_id',
                    'xcom_key': 'xcom_key',
                    'map_index': 'map_index',
                    'deserialize': 'deserialize',
                    'stringify': 'stringify',
                },
                'location_map': {
                    'dag_id': 'path',
                    'dag_run_id': 'path',
                    'task_id': 'path',
                    'xcom_key': 'path',
                    'map_index': 'query',
                    'deserialize': 'query',
                    'stringify': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def get_xcom_entries(
        self,
        dag_id,
        dag_run_id,
        task_id,
        **kwargs
    ):
        """List XCom entries  # noqa: E501

        This endpoint allows specifying `~` as the dag_id, dag_run_id, task_id to retrieve XCOM entries for for all DAGs, DAG runs and task instances. XCom values won't be returned as they can be large. Use this endpoint to get a list of XCom entries and then fetch individual entry to get value.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_xcom_entries(dag_id, dag_run_id, task_id, async_req=True)
        >>> result = thread.get()

        Args:
            dag_id (str): The DAG ID.
            dag_run_id (str): The DAG run ID.
            task_id (str): The task ID.

        Keyword Args:
            map_index (int): Filter on map index for mapped task.. [optional]
            xcom_key (str): Only filter the XCom records which have the provided key.. [optional]
            limit (int): The numbers of items to return.. [optional] if omitted the server will use the default value of 100
            offset (int): The number of items to skip before starting to collect the result set.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            XComCollection
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['dag_id'] = \
            dag_id
        kwargs['dag_run_id'] = \
            dag_run_id
        kwargs['task_id'] = \
            task_id
        return self.get_xcom_entries_endpoint.call_with_http_info(**kwargs)

    def get_xcom_entry(
        self,
        dag_id,
        dag_run_id,
        task_id,
        xcom_key,
        **kwargs
    ):
        """Get an XCom entry  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_xcom_entry(dag_id, dag_run_id, task_id, xcom_key, async_req=True)
        >>> result = thread.get()

        Args:
            dag_id (str): The DAG ID.
            dag_run_id (str): The DAG run ID.
            task_id (str): The task ID.
            xcom_key (str): The XCom key.

        Keyword Args:
            map_index (int): Filter on map index for mapped task.. [optional]
            deserialize (bool): Whether to deserialize an XCom value when using a custom XCom backend.  The XCom API endpoint calls `orm_deserialize_value` by default since an XCom may contain value that is potentially expensive to deserialize in the web server. Setting this to true overrides the consideration, and calls `deserialize_value` instead.  This parameter is not meaningful when using the default XCom backend.  *New in version 2.4.0* . [optional] if omitted the server will use the default value of False
            stringify (bool): Whether to convert the XCom value to be a string. XCom values can be of Any data type.  If set to true (default) the Any value will be returned as string, e.g. a Python representation of a dict. If set to false it will return the raw data as dict, list, string or whatever was stored.  *New in version 2.10.0* . [optional] if omitted the server will use the default value of True
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            XCom
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['dag_id'] = \
            dag_id
        kwargs['dag_run_id'] = \
            dag_run_id
        kwargs['task_id'] = \
            task_id
        kwargs['xcom_key'] = \
            xcom_key
        return self.get_xcom_entry_endpoint.call_with_http_info(**kwargs)

