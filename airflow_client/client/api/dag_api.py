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
from airflow_client.client.model.clear_task_instances import ClearTaskInstances
from airflow_client.client.model.dag import DAG
from airflow_client.client.model.dag_collection import DAGCollection
from airflow_client.client.model.dag_detail import DAGDetail
from airflow_client.client.model.error import Error
from airflow_client.client.model.inline_response200 import InlineResponse200
from airflow_client.client.model.task import Task
from airflow_client.client.model.task_collection import TaskCollection
from airflow_client.client.model.task_instance_reference_collection import TaskInstanceReferenceCollection
from airflow_client.client.model.update_task_instances_state import UpdateTaskInstancesState


class DAGApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.delete_dag_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'Basic',
                    'Kerberos'
                ],
                'endpoint_path': '/dags/{dag_id}',
                'operation_id': 'delete_dag',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'dag_id',
                ],
                'required': [
                    'dag_id',
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
                },
                'attribute_map': {
                    'dag_id': 'dag_id',
                },
                'location_map': {
                    'dag_id': 'path',
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
        self.get_dag_endpoint = _Endpoint(
            settings={
                'response_type': (DAG,),
                'auth': [
                    'Basic',
                    'Kerberos'
                ],
                'endpoint_path': '/dags/{dag_id}',
                'operation_id': 'get_dag',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'dag_id',
                    'fields',
                ],
                'required': [
                    'dag_id',
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
                    'fields':
                        ([str],),
                },
                'attribute_map': {
                    'dag_id': 'dag_id',
                    'fields': 'fields',
                },
                'location_map': {
                    'dag_id': 'path',
                    'fields': 'query',
                },
                'collection_format_map': {
                    'fields': 'multi',
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
        self.get_dag_details_endpoint = _Endpoint(
            settings={
                'response_type': (DAGDetail,),
                'auth': [
                    'Basic',
                    'Kerberos'
                ],
                'endpoint_path': '/dags/{dag_id}/details',
                'operation_id': 'get_dag_details',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'dag_id',
                    'fields',
                ],
                'required': [
                    'dag_id',
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
                    'fields':
                        ([str],),
                },
                'attribute_map': {
                    'dag_id': 'dag_id',
                    'fields': 'fields',
                },
                'location_map': {
                    'dag_id': 'path',
                    'fields': 'query',
                },
                'collection_format_map': {
                    'fields': 'multi',
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
        self.get_dag_source_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse200,),
                'auth': [
                    'Basic',
                    'Kerberos'
                ],
                'endpoint_path': '/dagSources/{file_token}',
                'operation_id': 'get_dag_source',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'file_token',
                ],
                'required': [
                    'file_token',
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
                    'file_token':
                        (str,),
                },
                'attribute_map': {
                    'file_token': 'file_token',
                },
                'location_map': {
                    'file_token': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'plain/text'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_dags_endpoint = _Endpoint(
            settings={
                'response_type': (DAGCollection,),
                'auth': [
                    'Basic',
                    'Kerberos'
                ],
                'endpoint_path': '/dags',
                'operation_id': 'get_dags',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'limit',
                    'offset',
                    'order_by',
                    'tags',
                    'only_active',
                    'paused',
                    'fields',
                    'dag_id_pattern',
                ],
                'required': [],
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
                    'limit':
                        (int,),
                    'offset':
                        (int,),
                    'order_by':
                        (str,),
                    'tags':
                        ([str],),
                    'only_active':
                        (bool,),
                    'paused':
                        (bool,),
                    'fields':
                        ([str],),
                    'dag_id_pattern':
                        (str,),
                },
                'attribute_map': {
                    'limit': 'limit',
                    'offset': 'offset',
                    'order_by': 'order_by',
                    'tags': 'tags',
                    'only_active': 'only_active',
                    'paused': 'paused',
                    'fields': 'fields',
                    'dag_id_pattern': 'dag_id_pattern',
                },
                'location_map': {
                    'limit': 'query',
                    'offset': 'query',
                    'order_by': 'query',
                    'tags': 'query',
                    'only_active': 'query',
                    'paused': 'query',
                    'fields': 'query',
                    'dag_id_pattern': 'query',
                },
                'collection_format_map': {
                    'tags': 'multi',
                    'fields': 'multi',
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
        self.get_task_endpoint = _Endpoint(
            settings={
                'response_type': (Task,),
                'auth': [
                    'Basic',
                    'Kerberos'
                ],
                'endpoint_path': '/dags/{dag_id}/tasks/{task_id}',
                'operation_id': 'get_task',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'dag_id',
                    'task_id',
                ],
                'required': [
                    'dag_id',
                    'task_id',
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
                    'task_id':
                        (str,),
                },
                'attribute_map': {
                    'dag_id': 'dag_id',
                    'task_id': 'task_id',
                },
                'location_map': {
                    'dag_id': 'path',
                    'task_id': 'path',
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
        self.get_tasks_endpoint = _Endpoint(
            settings={
                'response_type': (TaskCollection,),
                'auth': [
                    'Basic',
                    'Kerberos'
                ],
                'endpoint_path': '/dags/{dag_id}/tasks',
                'operation_id': 'get_tasks',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'dag_id',
                    'order_by',
                ],
                'required': [
                    'dag_id',
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
                    'order_by':
                        (str,),
                },
                'attribute_map': {
                    'dag_id': 'dag_id',
                    'order_by': 'order_by',
                },
                'location_map': {
                    'dag_id': 'path',
                    'order_by': 'query',
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
        self.patch_dag_endpoint = _Endpoint(
            settings={
                'response_type': (DAG,),
                'auth': [
                    'Basic',
                    'Kerberos'
                ],
                'endpoint_path': '/dags/{dag_id}',
                'operation_id': 'patch_dag',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'dag_id',
                    'dag',
                    'update_mask',
                ],
                'required': [
                    'dag_id',
                    'dag',
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
                    'dag':
                        (DAG,),
                    'update_mask':
                        ([str],),
                },
                'attribute_map': {
                    'dag_id': 'dag_id',
                    'update_mask': 'update_mask',
                },
                'location_map': {
                    'dag_id': 'path',
                    'dag': 'body',
                    'update_mask': 'query',
                },
                'collection_format_map': {
                    'update_mask': 'csv',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.patch_dags_endpoint = _Endpoint(
            settings={
                'response_type': (DAGCollection,),
                'auth': [
                    'Basic',
                    'Kerberos'
                ],
                'endpoint_path': '/dags',
                'operation_id': 'patch_dags',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'dag_id_pattern',
                    'dag',
                    'limit',
                    'offset',
                    'tags',
                    'update_mask',
                    'only_active',
                ],
                'required': [
                    'dag_id_pattern',
                    'dag',
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
                    'dag_id_pattern':
                        (str,),
                    'dag':
                        (DAG,),
                    'limit':
                        (int,),
                    'offset':
                        (int,),
                    'tags':
                        ([str],),
                    'update_mask':
                        ([str],),
                    'only_active':
                        (bool,),
                },
                'attribute_map': {
                    'dag_id_pattern': 'dag_id_pattern',
                    'limit': 'limit',
                    'offset': 'offset',
                    'tags': 'tags',
                    'update_mask': 'update_mask',
                    'only_active': 'only_active',
                },
                'location_map': {
                    'dag_id_pattern': 'query',
                    'dag': 'body',
                    'limit': 'query',
                    'offset': 'query',
                    'tags': 'query',
                    'update_mask': 'query',
                    'only_active': 'query',
                },
                'collection_format_map': {
                    'tags': 'multi',
                    'update_mask': 'csv',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.post_clear_task_instances_endpoint = _Endpoint(
            settings={
                'response_type': (TaskInstanceReferenceCollection,),
                'auth': [
                    'Basic',
                    'Kerberos'
                ],
                'endpoint_path': '/dags/{dag_id}/clearTaskInstances',
                'operation_id': 'post_clear_task_instances',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'dag_id',
                    'clear_task_instances',
                ],
                'required': [
                    'dag_id',
                    'clear_task_instances',
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
                    'clear_task_instances':
                        (ClearTaskInstances,),
                },
                'attribute_map': {
                    'dag_id': 'dag_id',
                },
                'location_map': {
                    'dag_id': 'path',
                    'clear_task_instances': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.post_set_task_instances_state_endpoint = _Endpoint(
            settings={
                'response_type': (TaskInstanceReferenceCollection,),
                'auth': [
                    'Basic',
                    'Kerberos'
                ],
                'endpoint_path': '/dags/{dag_id}/updateTaskInstancesState',
                'operation_id': 'post_set_task_instances_state',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'dag_id',
                    'update_task_instances_state',
                ],
                'required': [
                    'dag_id',
                    'update_task_instances_state',
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
                    'update_task_instances_state':
                        (UpdateTaskInstancesState,),
                },
                'attribute_map': {
                    'dag_id': 'dag_id',
                },
                'location_map': {
                    'dag_id': 'path',
                    'update_task_instances_state': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.reparse_dag_file_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'Basic',
                    'Kerberos'
                ],
                'endpoint_path': '/parseDagFile/{file_token}',
                'operation_id': 'reparse_dag_file',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'file_token',
                ],
                'required': [
                    'file_token',
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
                    'file_token':
                        (str,),
                },
                'attribute_map': {
                    'file_token': 'file_token',
                },
                'location_map': {
                    'file_token': 'path',
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

    def delete_dag(
        self,
        dag_id,
        **kwargs
    ):
        """Delete a DAG  # noqa: E501

        Deletes all metadata related to the DAG, including finished DAG Runs and Tasks. Logs are not deleted. This action cannot be undone.  *New in version 2.2.0*   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_dag(dag_id, async_req=True)
        >>> result = thread.get()

        Args:
            dag_id (str): The DAG ID.

        Keyword Args:
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
            None
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
        return self.delete_dag_endpoint.call_with_http_info(**kwargs)

    def get_dag(
        self,
        dag_id,
        **kwargs
    ):
        """Get basic information about a DAG  # noqa: E501

        Presents only information available in database (DAGModel). If you need detailed information, consider using GET /dags/{dag_id}/details.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dag(dag_id, async_req=True)
        >>> result = thread.get()

        Args:
            dag_id (str): The DAG ID.

        Keyword Args:
            fields ([str]): List of field for return. . [optional]
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
            DAG
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
        return self.get_dag_endpoint.call_with_http_info(**kwargs)

    def get_dag_details(
        self,
        dag_id,
        **kwargs
    ):
        """Get a simplified representation of DAG  # noqa: E501

        The response contains many DAG attributes, so the response can be large. If possible, consider using GET /dags/{dag_id}.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dag_details(dag_id, async_req=True)
        >>> result = thread.get()

        Args:
            dag_id (str): The DAG ID.

        Keyword Args:
            fields ([str]): List of field for return. . [optional]
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
            DAGDetail
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
        return self.get_dag_details_endpoint.call_with_http_info(**kwargs)

    def get_dag_source(
        self,
        file_token,
        **kwargs
    ):
        """Get a source code  # noqa: E501

        Get a source code using file token.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dag_source(file_token, async_req=True)
        >>> result = thread.get()

        Args:
            file_token (str): The key containing the encrypted path to the file. Encryption and decryption take place only on the server. This prevents the client from reading an non-DAG file. This also ensures API extensibility, because the format of encrypted data may change. 

        Keyword Args:
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
            InlineResponse200
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
        kwargs['file_token'] = \
            file_token
        return self.get_dag_source_endpoint.call_with_http_info(**kwargs)

    def get_dags(
        self,
        **kwargs
    ):
        """List DAGs  # noqa: E501

        List DAGs in the database. `dag_id_pattern` can be set to match dags of a specific pattern   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dags(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            limit (int): The numbers of items to return.. [optional] if omitted the server will use the default value of 100
            offset (int): The number of items to skip before starting to collect the result set.. [optional]
            order_by (str): The name of the field to order the results by. Prefix a field name with `-` to reverse the sort order.  *New in version 2.1.0* . [optional]
            tags ([str]): List of tags to filter results.  *New in version 2.2.0* . [optional]
            only_active (bool): Only filter active DAGs.  *New in version 2.1.1* . [optional] if omitted the server will use the default value of True
            paused (bool): Only filter paused/unpaused DAGs. If absent or null, it returns paused and unpaused DAGs.  *New in version 2.6.0* . [optional]
            fields ([str]): List of field for return. . [optional]
            dag_id_pattern (str): If set, only return DAGs with dag_ids matching this pattern. . [optional]
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
            DAGCollection
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
        return self.get_dags_endpoint.call_with_http_info(**kwargs)

    def get_task(
        self,
        dag_id,
        task_id,
        **kwargs
    ):
        """Get simplified representation of a task  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_task(dag_id, task_id, async_req=True)
        >>> result = thread.get()

        Args:
            dag_id (str): The DAG ID.
            task_id (str): The task ID.

        Keyword Args:
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
            Task
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
        kwargs['task_id'] = \
            task_id
        return self.get_task_endpoint.call_with_http_info(**kwargs)

    def get_tasks(
        self,
        dag_id,
        **kwargs
    ):
        """Get tasks for DAG  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_tasks(dag_id, async_req=True)
        >>> result = thread.get()

        Args:
            dag_id (str): The DAG ID.

        Keyword Args:
            order_by (str): The name of the field to order the results by. Prefix a field name with `-` to reverse the sort order.  *New in version 2.1.0* . [optional]
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
            TaskCollection
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
        return self.get_tasks_endpoint.call_with_http_info(**kwargs)

    def patch_dag(
        self,
        dag_id,
        dag,
        **kwargs
    ):
        """Update a DAG  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.patch_dag(dag_id, dag, async_req=True)
        >>> result = thread.get()

        Args:
            dag_id (str): The DAG ID.
            dag (DAG):

        Keyword Args:
            update_mask ([str]): The fields to update on the resource. If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields. . [optional]
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
            DAG
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
        kwargs['dag'] = \
            dag
        return self.patch_dag_endpoint.call_with_http_info(**kwargs)

    def patch_dags(
        self,
        dag_id_pattern,
        dag,
        **kwargs
    ):
        """Update DAGs  # noqa: E501

        Update DAGs of a given dag_id_pattern using UpdateMask. This endpoint allows specifying `~` as the dag_id_pattern to update all DAGs. *New in version 2.3.0*   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.patch_dags(dag_id_pattern, dag, async_req=True)
        >>> result = thread.get()

        Args:
            dag_id_pattern (str): If set, only update DAGs with dag_ids matching this pattern. 
            dag (DAG):

        Keyword Args:
            limit (int): The numbers of items to return.. [optional] if omitted the server will use the default value of 100
            offset (int): The number of items to skip before starting to collect the result set.. [optional]
            tags ([str]): List of tags to filter results.  *New in version 2.2.0* . [optional]
            update_mask ([str]): The fields to update on the resource. If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields. . [optional]
            only_active (bool): Only filter active DAGs.  *New in version 2.1.1* . [optional] if omitted the server will use the default value of True
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
            DAGCollection
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
        kwargs['dag_id_pattern'] = \
            dag_id_pattern
        kwargs['dag'] = \
            dag
        return self.patch_dags_endpoint.call_with_http_info(**kwargs)

    def post_clear_task_instances(
        self,
        dag_id,
        clear_task_instances,
        **kwargs
    ):
        """Clear a set of task instances  # noqa: E501

        Clears a set of task instances associated with the DAG for a specified date range.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.post_clear_task_instances(dag_id, clear_task_instances, async_req=True)
        >>> result = thread.get()

        Args:
            dag_id (str): The DAG ID.
            clear_task_instances (ClearTaskInstances): Parameters of action

        Keyword Args:
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
            TaskInstanceReferenceCollection
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
        kwargs['clear_task_instances'] = \
            clear_task_instances
        return self.post_clear_task_instances_endpoint.call_with_http_info(**kwargs)

    def post_set_task_instances_state(
        self,
        dag_id,
        update_task_instances_state,
        **kwargs
    ):
        """Set a state of task instances  # noqa: E501

        Updates the state for multiple task instances simultaneously.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.post_set_task_instances_state(dag_id, update_task_instances_state, async_req=True)
        >>> result = thread.get()

        Args:
            dag_id (str): The DAG ID.
            update_task_instances_state (UpdateTaskInstancesState): Parameters of action

        Keyword Args:
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
            TaskInstanceReferenceCollection
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
        kwargs['update_task_instances_state'] = \
            update_task_instances_state
        return self.post_set_task_instances_state_endpoint.call_with_http_info(**kwargs)

    def reparse_dag_file(
        self,
        file_token,
        **kwargs
    ):
        """Request re-parsing of a DAG file  # noqa: E501

        Request re-parsing of existing DAG files using a file token.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.reparse_dag_file(file_token, async_req=True)
        >>> result = thread.get()

        Args:
            file_token (str): The key containing the encrypted path to the file. Encryption and decryption take place only on the server. This prevents the client from reading an non-DAG file. This also ensures API extensibility, because the format of encrypted data may change. 

        Keyword Args:
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
            None
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
        kwargs['file_token'] = \
            file_token
        return self.reparse_dag_file_endpoint.call_with_http_info(**kwargs)

