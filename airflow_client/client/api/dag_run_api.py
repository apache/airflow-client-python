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
from airflow_client.client.model.clear_dag_run import ClearDagRun
from airflow_client.client.model.dag_run import DAGRun
from airflow_client.client.model.dag_run_collection import DAGRunCollection
from airflow_client.client.model.dataset_event_collection import DatasetEventCollection
from airflow_client.client.model.error import Error
from airflow_client.client.model.list_dag_runs_form import ListDagRunsForm
from airflow_client.client.model.set_dag_run_note import SetDagRunNote
from airflow_client.client.model.update_dag_run_state import UpdateDagRunState


class DAGRunApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.clear_dag_run_endpoint = _Endpoint(
            settings={
                'response_type': (bool, date, datetime, dict, float, int, list, str, none_type,),
                'auth': [
                    'Basic',
                    'Kerberos'
                ],
                'endpoint_path': '/dags/{dag_id}/dagRuns/{dag_run_id}/clear',
                'operation_id': 'clear_dag_run',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'dag_id',
                    'dag_run_id',
                    'clear_dag_run',
                ],
                'required': [
                    'dag_id',
                    'dag_run_id',
                    'clear_dag_run',
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
                    'clear_dag_run':
                        (ClearDagRun,),
                },
                'attribute_map': {
                    'dag_id': 'dag_id',
                    'dag_run_id': 'dag_run_id',
                },
                'location_map': {
                    'dag_id': 'path',
                    'dag_run_id': 'path',
                    'clear_dag_run': 'body',
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
        self.delete_dag_run_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'Basic',
                    'Kerberos'
                ],
                'endpoint_path': '/dags/{dag_id}/dagRuns/{dag_run_id}',
                'operation_id': 'delete_dag_run',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'dag_id',
                    'dag_run_id',
                ],
                'required': [
                    'dag_id',
                    'dag_run_id',
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
                },
                'attribute_map': {
                    'dag_id': 'dag_id',
                    'dag_run_id': 'dag_run_id',
                },
                'location_map': {
                    'dag_id': 'path',
                    'dag_run_id': 'path',
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
        self.get_dag_run_endpoint = _Endpoint(
            settings={
                'response_type': (DAGRun,),
                'auth': [
                    'Basic',
                    'Kerberos'
                ],
                'endpoint_path': '/dags/{dag_id}/dagRuns/{dag_run_id}',
                'operation_id': 'get_dag_run',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'dag_id',
                    'dag_run_id',
                    'fields',
                ],
                'required': [
                    'dag_id',
                    'dag_run_id',
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
                    'fields':
                        ([str],),
                },
                'attribute_map': {
                    'dag_id': 'dag_id',
                    'dag_run_id': 'dag_run_id',
                    'fields': 'fields',
                },
                'location_map': {
                    'dag_id': 'path',
                    'dag_run_id': 'path',
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
        self.get_dag_runs_endpoint = _Endpoint(
            settings={
                'response_type': (DAGRunCollection,),
                'auth': [
                    'Basic',
                    'Kerberos'
                ],
                'endpoint_path': '/dags/{dag_id}/dagRuns',
                'operation_id': 'get_dag_runs',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'dag_id',
                    'limit',
                    'offset',
                    'execution_date_gte',
                    'execution_date_lte',
                    'start_date_gte',
                    'start_date_lte',
                    'end_date_gte',
                    'end_date_lte',
                    'updated_at_gte',
                    'updated_at_lte',
                    'state',
                    'order_by',
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
                    'limit':
                        (int,),
                    'offset':
                        (int,),
                    'execution_date_gte':
                        (datetime,),
                    'execution_date_lte':
                        (datetime,),
                    'start_date_gte':
                        (datetime,),
                    'start_date_lte':
                        (datetime,),
                    'end_date_gte':
                        (datetime,),
                    'end_date_lte':
                        (datetime,),
                    'updated_at_gte':
                        (datetime,),
                    'updated_at_lte':
                        (datetime,),
                    'state':
                        ([str],),
                    'order_by':
                        (str,),
                    'fields':
                        ([str],),
                },
                'attribute_map': {
                    'dag_id': 'dag_id',
                    'limit': 'limit',
                    'offset': 'offset',
                    'execution_date_gte': 'execution_date_gte',
                    'execution_date_lte': 'execution_date_lte',
                    'start_date_gte': 'start_date_gte',
                    'start_date_lte': 'start_date_lte',
                    'end_date_gte': 'end_date_gte',
                    'end_date_lte': 'end_date_lte',
                    'updated_at_gte': 'updated_at_gte',
                    'updated_at_lte': 'updated_at_lte',
                    'state': 'state',
                    'order_by': 'order_by',
                    'fields': 'fields',
                },
                'location_map': {
                    'dag_id': 'path',
                    'limit': 'query',
                    'offset': 'query',
                    'execution_date_gte': 'query',
                    'execution_date_lte': 'query',
                    'start_date_gte': 'query',
                    'start_date_lte': 'query',
                    'end_date_gte': 'query',
                    'end_date_lte': 'query',
                    'updated_at_gte': 'query',
                    'updated_at_lte': 'query',
                    'state': 'query',
                    'order_by': 'query',
                    'fields': 'query',
                },
                'collection_format_map': {
                    'state': 'multi',
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
        self.get_dag_runs_batch_endpoint = _Endpoint(
            settings={
                'response_type': (DAGRunCollection,),
                'auth': [
                    'Basic',
                    'Kerberos'
                ],
                'endpoint_path': '/dags/~/dagRuns/list',
                'operation_id': 'get_dag_runs_batch',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'list_dag_runs_form',
                ],
                'required': [
                    'list_dag_runs_form',
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
                    'list_dag_runs_form':
                        (ListDagRunsForm,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'list_dag_runs_form': 'body',
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
        self.get_upstream_dataset_events_endpoint = _Endpoint(
            settings={
                'response_type': (DatasetEventCollection,),
                'auth': [
                    'Basic',
                    'Kerberos'
                ],
                'endpoint_path': '/dags/{dag_id}/dagRuns/{dag_run_id}/upstreamDatasetEvents',
                'operation_id': 'get_upstream_dataset_events',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'dag_id',
                    'dag_run_id',
                ],
                'required': [
                    'dag_id',
                    'dag_run_id',
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
                },
                'attribute_map': {
                    'dag_id': 'dag_id',
                    'dag_run_id': 'dag_run_id',
                },
                'location_map': {
                    'dag_id': 'path',
                    'dag_run_id': 'path',
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
        self.post_dag_run_endpoint = _Endpoint(
            settings={
                'response_type': (DAGRun,),
                'auth': [
                    'Basic',
                    'Kerberos'
                ],
                'endpoint_path': '/dags/{dag_id}/dagRuns',
                'operation_id': 'post_dag_run',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'dag_id',
                    'dag_run',
                ],
                'required': [
                    'dag_id',
                    'dag_run',
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
                    'dag_run':
                        (DAGRun,),
                },
                'attribute_map': {
                    'dag_id': 'dag_id',
                },
                'location_map': {
                    'dag_id': 'path',
                    'dag_run': 'body',
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
        self.set_dag_run_note_endpoint = _Endpoint(
            settings={
                'response_type': (DAGRun,),
                'auth': [
                    'Basic',
                    'Kerberos'
                ],
                'endpoint_path': '/dags/{dag_id}/dagRuns/{dag_run_id}/setNote',
                'operation_id': 'set_dag_run_note',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'dag_id',
                    'dag_run_id',
                    'set_dag_run_note',
                ],
                'required': [
                    'dag_id',
                    'dag_run_id',
                    'set_dag_run_note',
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
                    'set_dag_run_note':
                        (SetDagRunNote,),
                },
                'attribute_map': {
                    'dag_id': 'dag_id',
                    'dag_run_id': 'dag_run_id',
                },
                'location_map': {
                    'dag_id': 'path',
                    'dag_run_id': 'path',
                    'set_dag_run_note': 'body',
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
        self.update_dag_run_state_endpoint = _Endpoint(
            settings={
                'response_type': (DAGRun,),
                'auth': [
                    'Basic',
                    'Kerberos'
                ],
                'endpoint_path': '/dags/{dag_id}/dagRuns/{dag_run_id}',
                'operation_id': 'update_dag_run_state',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'dag_id',
                    'dag_run_id',
                    'update_dag_run_state',
                ],
                'required': [
                    'dag_id',
                    'dag_run_id',
                    'update_dag_run_state',
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
                    'update_dag_run_state':
                        (UpdateDagRunState,),
                },
                'attribute_map': {
                    'dag_id': 'dag_id',
                    'dag_run_id': 'dag_run_id',
                },
                'location_map': {
                    'dag_id': 'path',
                    'dag_run_id': 'path',
                    'update_dag_run_state': 'body',
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

    def clear_dag_run(
        self,
        dag_id,
        dag_run_id,
        clear_dag_run,
        **kwargs
    ):
        """Clear a DAG run  # noqa: E501

        Clear a DAG run.  *New in version 2.4.0*   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.clear_dag_run(dag_id, dag_run_id, clear_dag_run, async_req=True)
        >>> result = thread.get()

        Args:
            dag_id (str): The DAG ID.
            dag_run_id (str): The DAG run ID.
            clear_dag_run (ClearDagRun):

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
            bool, date, datetime, dict, float, int, list, str, none_type
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
        kwargs['clear_dag_run'] = \
            clear_dag_run
        return self.clear_dag_run_endpoint.call_with_http_info(**kwargs)

    def delete_dag_run(
        self,
        dag_id,
        dag_run_id,
        **kwargs
    ):
        """Delete a DAG run  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_dag_run(dag_id, dag_run_id, async_req=True)
        >>> result = thread.get()

        Args:
            dag_id (str): The DAG ID.
            dag_run_id (str): The DAG run ID.

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
        kwargs['dag_run_id'] = \
            dag_run_id
        return self.delete_dag_run_endpoint.call_with_http_info(**kwargs)

    def get_dag_run(
        self,
        dag_id,
        dag_run_id,
        **kwargs
    ):
        """Get a DAG run  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dag_run(dag_id, dag_run_id, async_req=True)
        >>> result = thread.get()

        Args:
            dag_id (str): The DAG ID.
            dag_run_id (str): The DAG run ID.

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
            DAGRun
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
        return self.get_dag_run_endpoint.call_with_http_info(**kwargs)

    def get_dag_runs(
        self,
        dag_id,
        **kwargs
    ):
        """List DAG runs  # noqa: E501

        This endpoint allows specifying `~` as the dag_id to retrieve DAG runs for all DAGs.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dag_runs(dag_id, async_req=True)
        >>> result = thread.get()

        Args:
            dag_id (str): The DAG ID.

        Keyword Args:
            limit (int): The numbers of items to return.. [optional] if omitted the server will use the default value of 100
            offset (int): The number of items to skip before starting to collect the result set.. [optional]
            execution_date_gte (datetime): Returns objects greater or equal to the specified date.  This can be combined with execution_date_lte parameter to receive only the selected period. . [optional]
            execution_date_lte (datetime): Returns objects less than or equal to the specified date.  This can be combined with execution_date_gte parameter to receive only the selected period. . [optional]
            start_date_gte (datetime): Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period. . [optional]
            start_date_lte (datetime): Returns objects less or equal the specified date.  This can be combined with start_date_gte parameter to receive only the selected period. . [optional]
            end_date_gte (datetime): Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period. . [optional]
            end_date_lte (datetime): Returns objects less than or equal to the specified date.  This can be combined with start_date_gte parameter to receive only the selected period. . [optional]
            updated_at_gte (datetime): Returns objects greater or equal the specified date.  This can be combined with updated_at_lte parameter to receive only the selected period.  *New in version 2.6.0* . [optional]
            updated_at_lte (datetime): Returns objects less or equal the specified date.  This can be combined with updated_at_gte parameter to receive only the selected period.  *New in version 2.6.0* . [optional]
            state ([str]): The value can be repeated to retrieve multiple matching values (OR condition).. [optional]
            order_by (str): The name of the field to order the results by. Prefix a field name with `-` to reverse the sort order.  *New in version 2.1.0* . [optional]
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
            DAGRunCollection
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
        return self.get_dag_runs_endpoint.call_with_http_info(**kwargs)

    def get_dag_runs_batch(
        self,
        list_dag_runs_form,
        **kwargs
    ):
        """List DAG runs (batch)  # noqa: E501

        This endpoint is a POST to allow filtering across a large number of DAG IDs, where as a GET it would run in to maximum HTTP request URL length limit.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dag_runs_batch(list_dag_runs_form, async_req=True)
        >>> result = thread.get()

        Args:
            list_dag_runs_form (ListDagRunsForm):

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
            DAGRunCollection
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
        kwargs['list_dag_runs_form'] = \
            list_dag_runs_form
        return self.get_dag_runs_batch_endpoint.call_with_http_info(**kwargs)

    def get_upstream_dataset_events(
        self,
        dag_id,
        dag_run_id,
        **kwargs
    ):
        """Get dataset events for a DAG run  # noqa: E501

        Get datasets for a dag run.  *New in version 2.4.0*   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_upstream_dataset_events(dag_id, dag_run_id, async_req=True)
        >>> result = thread.get()

        Args:
            dag_id (str): The DAG ID.
            dag_run_id (str): The DAG run ID.

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
            DatasetEventCollection
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
        return self.get_upstream_dataset_events_endpoint.call_with_http_info(**kwargs)

    def post_dag_run(
        self,
        dag_id,
        dag_run,
        **kwargs
    ):
        """Trigger a new DAG run.  # noqa: E501

        This will initiate a dagrun. If DAG is paused then dagrun state will remain queued, and the task won't run.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.post_dag_run(dag_id, dag_run, async_req=True)
        >>> result = thread.get()

        Args:
            dag_id (str): The DAG ID.
            dag_run (DAGRun):

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
            DAGRun
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
        kwargs['dag_run'] = \
            dag_run
        return self.post_dag_run_endpoint.call_with_http_info(**kwargs)

    def set_dag_run_note(
        self,
        dag_id,
        dag_run_id,
        set_dag_run_note,
        **kwargs
    ):
        """Update the DagRun note.  # noqa: E501

        Update the manual user note of a DagRun.  *New in version 2.5.0*   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.set_dag_run_note(dag_id, dag_run_id, set_dag_run_note, async_req=True)
        >>> result = thread.get()

        Args:
            dag_id (str): The DAG ID.
            dag_run_id (str): The DAG run ID.
            set_dag_run_note (SetDagRunNote): Parameters of set DagRun note.

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
            DAGRun
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
        kwargs['set_dag_run_note'] = \
            set_dag_run_note
        return self.set_dag_run_note_endpoint.call_with_http_info(**kwargs)

    def update_dag_run_state(
        self,
        dag_id,
        dag_run_id,
        update_dag_run_state,
        **kwargs
    ):
        """Modify a DAG run  # noqa: E501

        Modify a DAG run.  *New in version 2.2.0*   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_dag_run_state(dag_id, dag_run_id, update_dag_run_state, async_req=True)
        >>> result = thread.get()

        Args:
            dag_id (str): The DAG ID.
            dag_run_id (str): The DAG run ID.
            update_dag_run_state (UpdateDagRunState):

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
            DAGRun
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
        kwargs['update_dag_run_state'] = \
            update_dag_run_state
        return self.update_dag_run_state_endpoint.call_with_http_info(**kwargs)

