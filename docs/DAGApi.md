# airflow_client.client.DAGApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_dag**](DAGApi.md#delete_dag) | **DELETE** /dags/{dag_id} | Delete a DAG
[**get_dag**](DAGApi.md#get_dag) | **GET** /dags/{dag_id} | Get basic information about a DAG
[**get_dag_details**](DAGApi.md#get_dag_details) | **GET** /dags/{dag_id}/details | Get a simplified representation of DAG
[**get_dag_source**](DAGApi.md#get_dag_source) | **GET** /dagSources/{file_token} | Get a source code
[**get_dags**](DAGApi.md#get_dags) | **GET** /dags | List DAGs
[**get_task**](DAGApi.md#get_task) | **GET** /dags/{dag_id}/tasks/{task_id} | Get simplified representation of a task
[**get_tasks**](DAGApi.md#get_tasks) | **GET** /dags/{dag_id}/tasks | Get tasks for DAG
[**patch_dag**](DAGApi.md#patch_dag) | **PATCH** /dags/{dag_id} | Update a DAG
[**patch_dags**](DAGApi.md#patch_dags) | **PATCH** /dags | Update DAGs
[**post_clear_task_instances**](DAGApi.md#post_clear_task_instances) | **POST** /dags/{dag_id}/clearTaskInstances | Clear a set of task instances
[**post_set_task_instances_state**](DAGApi.md#post_set_task_instances_state) | **POST** /dags/{dag_id}/updateTaskInstancesState | Set a state of task instances
[**reparse_dag_file**](DAGApi.md#reparse_dag_file) | **PUT** /parseDagFile/{file_token} | Request re-parsing of a DAG file


# **delete_dag**
> delete_dag(dag_id)

Delete a DAG

Deletes all metadata related to the DAG, including finished DAG Runs and Tasks. Logs are not deleted. This action cannot be undone.  *New in version 2.2.0* 

### Example

* Basic Authentication (Basic):

```python
import time
import airflow_client.client
from airflow_client.client.api import dag_api
from airflow_client.client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = airflow_client.client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = airflow_client.client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dag_api.DAGApi(api_client)
    dag_id = "dag_id_example" # str | The DAG ID.

    # example passing only required values which don't have defaults set
    try:
        # Delete a DAG
        api_instance.delete_dag(dag_id)
    except airflow_client.client.ApiException as e:
        print("Exception when calling DAGApi->delete_dag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. |

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [Kerberos](../README.md#Kerberos)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success. |  -  |
**400** | Client specified an invalid argument. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |
**404** | A specified resource is not found. |  -  |
**409** | An existing resource conflicts with the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dag**
> DAG get_dag(dag_id)

Get basic information about a DAG

Presents only information available in database (DAGModel). If you need detailed information, consider using GET /dags/{dag_id}/details. 

### Example

* Basic Authentication (Basic):

```python
import time
import airflow_client.client
from airflow_client.client.api import dag_api
from airflow_client.client.model.error import Error
from airflow_client.client.model.dag import DAG
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = airflow_client.client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = airflow_client.client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dag_api.DAGApi(api_client)
    dag_id = "dag_id_example" # str | The DAG ID.
    fields = [
        "fields_example",
    ] # [str] | List of field for return.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get basic information about a DAG
        api_response = api_instance.get_dag(dag_id)
        pprint(api_response)
    except airflow_client.client.ApiException as e:
        print("Exception when calling DAGApi->get_dag: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get basic information about a DAG
        api_response = api_instance.get_dag(dag_id, fields=fields)
        pprint(api_response)
    except airflow_client.client.ApiException as e:
        print("Exception when calling DAGApi->get_dag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. |
 **fields** | **[str]**| List of field for return.  | [optional]

### Return type

[**DAG**](DAG.md)

### Authorization

[Basic](../README.md#Basic), [Kerberos](../README.md#Kerberos)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |
**404** | A specified resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dag_details**
> DAGDetail get_dag_details(dag_id)

Get a simplified representation of DAG

The response contains many DAG attributes, so the response can be large. If possible, consider using GET /dags/{dag_id}. 

### Example

* Basic Authentication (Basic):

```python
import time
import airflow_client.client
from airflow_client.client.api import dag_api
from airflow_client.client.model.dag_detail import DAGDetail
from airflow_client.client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = airflow_client.client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = airflow_client.client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dag_api.DAGApi(api_client)
    dag_id = "dag_id_example" # str | The DAG ID.
    fields = [
        "fields_example",
    ] # [str] | List of field for return.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a simplified representation of DAG
        api_response = api_instance.get_dag_details(dag_id)
        pprint(api_response)
    except airflow_client.client.ApiException as e:
        print("Exception when calling DAGApi->get_dag_details: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a simplified representation of DAG
        api_response = api_instance.get_dag_details(dag_id, fields=fields)
        pprint(api_response)
    except airflow_client.client.ApiException as e:
        print("Exception when calling DAGApi->get_dag_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. |
 **fields** | **[str]**| List of field for return.  | [optional]

### Return type

[**DAGDetail**](DAGDetail.md)

### Authorization

[Basic](../README.md#Basic), [Kerberos](../README.md#Kerberos)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |
**404** | A specified resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dag_source**
> InlineResponse200 get_dag_source(file_token)

Get a source code

Get a source code using file token. 

### Example

* Basic Authentication (Basic):

```python
import time
import airflow_client.client
from airflow_client.client.api import dag_api
from airflow_client.client.model.error import Error
from airflow_client.client.model.inline_response200 import InlineResponse200
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = airflow_client.client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = airflow_client.client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dag_api.DAGApi(api_client)
    file_token = "file_token_example" # str | The key containing the encrypted path to the file. Encryption and decryption take place only on the server. This prevents the client from reading an non-DAG file. This also ensures API extensibility, because the format of encrypted data may change. 

    # example passing only required values which don't have defaults set
    try:
        # Get a source code
        api_response = api_instance.get_dag_source(file_token)
        pprint(api_response)
    except airflow_client.client.ApiException as e:
        print("Exception when calling DAGApi->get_dag_source: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_token** | **str**| The key containing the encrypted path to the file. Encryption and decryption take place only on the server. This prevents the client from reading an non-DAG file. This also ensures API extensibility, because the format of encrypted data may change.  |

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[Basic](../README.md#Basic), [Kerberos](../README.md#Kerberos)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, plain/text


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |
**404** | A specified resource is not found. |  -  |
**406** | A specified Accept header is not allowed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dags**
> DAGCollection get_dags()

List DAGs

List DAGs in the database. `dag_id_pattern` can be set to match dags of a specific pattern 

### Example

* Basic Authentication (Basic):

```python
import time
import airflow_client.client
from airflow_client.client.api import dag_api
from airflow_client.client.model.dag_collection import DAGCollection
from airflow_client.client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = airflow_client.client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = airflow_client.client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dag_api.DAGApi(api_client)
    limit = 100 # int | The numbers of items to return. (optional) if omitted the server will use the default value of 100
    offset = 0 # int | The number of items to skip before starting to collect the result set. (optional)
    order_by = "order_by_example" # str | The name of the field to order the results by. Prefix a field name with `-` to reverse the sort order.  *New in version 2.1.0*  (optional)
    tags = [
        "tags_example",
    ] # [str] | List of tags to filter results.  *New in version 2.2.0*  (optional)
    only_active = True # bool | Only filter active DAGs.  *New in version 2.1.1*  (optional) if omitted the server will use the default value of True
    paused = True # bool | Only filter paused/unpaused DAGs. If absent or null, it returns paused and unpaused DAGs.  *New in version 2.6.0*  (optional)
    fields = [
        "fields_example",
    ] # [str] | List of field for return.  (optional)
    dag_id_pattern = "dag_id_pattern_example" # str | If set, only return DAGs with dag_ids matching this pattern.  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List DAGs
        api_response = api_instance.get_dags(limit=limit, offset=offset, order_by=order_by, tags=tags, only_active=only_active, paused=paused, fields=fields, dag_id_pattern=dag_id_pattern)
        pprint(api_response)
    except airflow_client.client.ApiException as e:
        print("Exception when calling DAGApi->get_dags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The numbers of items to return. | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional]
 **order_by** | **str**| The name of the field to order the results by. Prefix a field name with &#x60;-&#x60; to reverse the sort order.  *New in version 2.1.0*  | [optional]
 **tags** | **[str]**| List of tags to filter results.  *New in version 2.2.0*  | [optional]
 **only_active** | **bool**| Only filter active DAGs.  *New in version 2.1.1*  | [optional] if omitted the server will use the default value of True
 **paused** | **bool**| Only filter paused/unpaused DAGs. If absent or null, it returns paused and unpaused DAGs.  *New in version 2.6.0*  | [optional]
 **fields** | **[str]**| List of field for return.  | [optional]
 **dag_id_pattern** | **str**| If set, only return DAGs with dag_ids matching this pattern.  | [optional]

### Return type

[**DAGCollection**](DAGCollection.md)

### Authorization

[Basic](../README.md#Basic), [Kerberos](../README.md#Kerberos)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task**
> Task get_task(dag_id, task_id)

Get simplified representation of a task

### Example

* Basic Authentication (Basic):

```python
import time
import airflow_client.client
from airflow_client.client.api import dag_api
from airflow_client.client.model.task import Task
from airflow_client.client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = airflow_client.client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = airflow_client.client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dag_api.DAGApi(api_client)
    dag_id = "dag_id_example" # str | The DAG ID.
    task_id = "task_id_example" # str | The task ID.

    # example passing only required values which don't have defaults set
    try:
        # Get simplified representation of a task
        api_response = api_instance.get_task(dag_id, task_id)
        pprint(api_response)
    except airflow_client.client.ApiException as e:
        print("Exception when calling DAGApi->get_task: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. |
 **task_id** | **str**| The task ID. |

### Return type

[**Task**](Task.md)

### Authorization

[Basic](../README.md#Basic), [Kerberos](../README.md#Kerberos)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |
**404** | A specified resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks**
> TaskCollection get_tasks(dag_id)

Get tasks for DAG

### Example

* Basic Authentication (Basic):

```python
import time
import airflow_client.client
from airflow_client.client.api import dag_api
from airflow_client.client.model.task_collection import TaskCollection
from airflow_client.client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = airflow_client.client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = airflow_client.client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dag_api.DAGApi(api_client)
    dag_id = "dag_id_example" # str | The DAG ID.
    order_by = "order_by_example" # str | The name of the field to order the results by. Prefix a field name with `-` to reverse the sort order.  *New in version 2.1.0*  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get tasks for DAG
        api_response = api_instance.get_tasks(dag_id)
        pprint(api_response)
    except airflow_client.client.ApiException as e:
        print("Exception when calling DAGApi->get_tasks: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get tasks for DAG
        api_response = api_instance.get_tasks(dag_id, order_by=order_by)
        pprint(api_response)
    except airflow_client.client.ApiException as e:
        print("Exception when calling DAGApi->get_tasks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. |
 **order_by** | **str**| The name of the field to order the results by. Prefix a field name with &#x60;-&#x60; to reverse the sort order.  *New in version 2.1.0*  | [optional]

### Return type

[**TaskCollection**](TaskCollection.md)

### Authorization

[Basic](../README.md#Basic), [Kerberos](../README.md#Kerberos)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |
**404** | A specified resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_dag**
> DAG patch_dag(dag_id, dag)

Update a DAG

### Example

* Basic Authentication (Basic):

```python
import time
import airflow_client.client
from airflow_client.client.api import dag_api
from airflow_client.client.model.error import Error
from airflow_client.client.model.dag import DAG
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = airflow_client.client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = airflow_client.client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dag_api.DAGApi(api_client)
    dag_id = "dag_id_example" # str | The DAG ID.
    dag = DAG(
        is_paused=True,
    ) # DAG | 
    update_mask = [
        "update_mask_example",
    ] # [str] | The fields to update on the resource. If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a DAG
        api_response = api_instance.patch_dag(dag_id, dag)
        pprint(api_response)
    except airflow_client.client.ApiException as e:
        print("Exception when calling DAGApi->patch_dag: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a DAG
        api_response = api_instance.patch_dag(dag_id, dag, update_mask=update_mask)
        pprint(api_response)
    except airflow_client.client.ApiException as e:
        print("Exception when calling DAGApi->patch_dag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. |
 **dag** | [**DAG**](DAG.md)|  |
 **update_mask** | **[str]**| The fields to update on the resource. If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields.  | [optional]

### Return type

[**DAG**](DAG.md)

### Authorization

[Basic](../README.md#Basic), [Kerberos](../README.md#Kerberos)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |
**404** | A specified resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_dags**
> DAGCollection patch_dags(dag_id_pattern, dag)

Update DAGs

Update DAGs of a given dag_id_pattern using UpdateMask. This endpoint allows specifying `~` as the dag_id_pattern to update all DAGs. *New in version 2.3.0* 

### Example

* Basic Authentication (Basic):

```python
import time
import airflow_client.client
from airflow_client.client.api import dag_api
from airflow_client.client.model.dag_collection import DAGCollection
from airflow_client.client.model.error import Error
from airflow_client.client.model.dag import DAG
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = airflow_client.client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = airflow_client.client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dag_api.DAGApi(api_client)
    dag_id_pattern = "dag_id_pattern_example" # str | If set, only update DAGs with dag_ids matching this pattern. 
    dag = DAG(
        is_paused=True,
    ) # DAG | 
    limit = 100 # int | The numbers of items to return. (optional) if omitted the server will use the default value of 100
    offset = 0 # int | The number of items to skip before starting to collect the result set. (optional)
    tags = [
        "tags_example",
    ] # [str] | List of tags to filter results.  *New in version 2.2.0*  (optional)
    update_mask = [
        "update_mask_example",
    ] # [str] | The fields to update on the resource. If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields.  (optional)
    only_active = True # bool | Only filter active DAGs.  *New in version 2.1.1*  (optional) if omitted the server will use the default value of True

    # example passing only required values which don't have defaults set
    try:
        # Update DAGs
        api_response = api_instance.patch_dags(dag_id_pattern, dag)
        pprint(api_response)
    except airflow_client.client.ApiException as e:
        print("Exception when calling DAGApi->patch_dags: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update DAGs
        api_response = api_instance.patch_dags(dag_id_pattern, dag, limit=limit, offset=offset, tags=tags, update_mask=update_mask, only_active=only_active)
        pprint(api_response)
    except airflow_client.client.ApiException as e:
        print("Exception when calling DAGApi->patch_dags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id_pattern** | **str**| If set, only update DAGs with dag_ids matching this pattern.  |
 **dag** | [**DAG**](DAG.md)|  |
 **limit** | **int**| The numbers of items to return. | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional]
 **tags** | **[str]**| List of tags to filter results.  *New in version 2.2.0*  | [optional]
 **update_mask** | **[str]**| The fields to update on the resource. If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields.  | [optional]
 **only_active** | **bool**| Only filter active DAGs.  *New in version 2.1.1*  | [optional] if omitted the server will use the default value of True

### Return type

[**DAGCollection**](DAGCollection.md)

### Authorization

[Basic](../README.md#Basic), [Kerberos](../README.md#Kerberos)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |
**404** | A specified resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_clear_task_instances**
> TaskInstanceReferenceCollection post_clear_task_instances(dag_id, clear_task_instances)

Clear a set of task instances

Clears a set of task instances associated with the DAG for a specified date range. 

### Example

* Basic Authentication (Basic):

```python
import time
import airflow_client.client
from airflow_client.client.api import dag_api
from airflow_client.client.model.clear_task_instances import ClearTaskInstances
from airflow_client.client.model.error import Error
from airflow_client.client.model.task_instance_reference_collection import TaskInstanceReferenceCollection
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = airflow_client.client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = airflow_client.client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dag_api.DAGApi(api_client)
    dag_id = "dag_id_example" # str | The DAG ID.
    clear_task_instances = ClearTaskInstances(
        dag_run_id="dag_run_id_example",
        dry_run=True,
        end_date="end_date_example",
        include_downstream=False,
        include_future=False,
        include_parentdag=True,
        include_past=False,
        include_subdags=True,
        include_upstream=False,
        only_failed=True,
        only_running=False,
        reset_dag_runs=True,
        start_date="start_date_example",
        task_ids=[
            "task_ids_example",
        ],
    ) # ClearTaskInstances | Parameters of action

    # example passing only required values which don't have defaults set
    try:
        # Clear a set of task instances
        api_response = api_instance.post_clear_task_instances(dag_id, clear_task_instances)
        pprint(api_response)
    except airflow_client.client.ApiException as e:
        print("Exception when calling DAGApi->post_clear_task_instances: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. |
 **clear_task_instances** | [**ClearTaskInstances**](ClearTaskInstances.md)| Parameters of action |

### Return type

[**TaskInstanceReferenceCollection**](TaskInstanceReferenceCollection.md)

### Authorization

[Basic](../README.md#Basic), [Kerberos](../README.md#Kerberos)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |
**404** | A specified resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_set_task_instances_state**
> TaskInstanceReferenceCollection post_set_task_instances_state(dag_id, update_task_instances_state)

Set a state of task instances

Updates the state for multiple task instances simultaneously. 

### Example

* Basic Authentication (Basic):

```python
import time
import airflow_client.client
from airflow_client.client.api import dag_api
from airflow_client.client.model.error import Error
from airflow_client.client.model.update_task_instances_state import UpdateTaskInstancesState
from airflow_client.client.model.task_instance_reference_collection import TaskInstanceReferenceCollection
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = airflow_client.client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = airflow_client.client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dag_api.DAGApi(api_client)
    dag_id = "dag_id_example" # str | The DAG ID.
    update_task_instances_state = UpdateTaskInstancesState(
        dag_run_id="dag_run_id_example",
        dry_run=True,
        execution_date="execution_date_example",
        include_downstream=True,
        include_future=True,
        include_past=True,
        include_upstream=True,
        new_state=UpdateTaskState("success"),
        task_id="task_id_example",
    ) # UpdateTaskInstancesState | Parameters of action

    # example passing only required values which don't have defaults set
    try:
        # Set a state of task instances
        api_response = api_instance.post_set_task_instances_state(dag_id, update_task_instances_state)
        pprint(api_response)
    except airflow_client.client.ApiException as e:
        print("Exception when calling DAGApi->post_set_task_instances_state: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. |
 **update_task_instances_state** | [**UpdateTaskInstancesState**](UpdateTaskInstancesState.md)| Parameters of action |

### Return type

[**TaskInstanceReferenceCollection**](TaskInstanceReferenceCollection.md)

### Authorization

[Basic](../README.md#Basic), [Kerberos](../README.md#Kerberos)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |
**404** | A specified resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reparse_dag_file**
> reparse_dag_file(file_token)

Request re-parsing of a DAG file

Request re-parsing of existing DAG files using a file token. 

### Example

* Basic Authentication (Basic):

```python
import time
import airflow_client.client
from airflow_client.client.api import dag_api
from airflow_client.client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = airflow_client.client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = airflow_client.client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dag_api.DAGApi(api_client)
    file_token = "file_token_example" # str | The key containing the encrypted path to the file. Encryption and decryption take place only on the server. This prevents the client from reading an non-DAG file. This also ensures API extensibility, because the format of encrypted data may change. 

    # example passing only required values which don't have defaults set
    try:
        # Request re-parsing of a DAG file
        api_instance.reparse_dag_file(file_token)
    except airflow_client.client.ApiException as e:
        print("Exception when calling DAGApi->reparse_dag_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_token** | **str**| The key containing the encrypted path to the file. Encryption and decryption take place only on the server. This prevents the client from reading an non-DAG file. This also ensures API extensibility, because the format of encrypted data may change.  |

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [Kerberos](../README.md#Kerberos)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |
**404** | A specified resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

