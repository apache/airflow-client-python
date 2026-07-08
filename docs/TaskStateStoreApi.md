# airflow_client.client.TaskStateStoreApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_task_state_store**](TaskStateStoreApi.md#clear_task_state_store) | **DELETE** /api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/state-store | Clear Task State Store
[**delete_task_state_store**](TaskStateStoreApi.md#delete_task_state_store) | **DELETE** /api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/state-store/{key} | Delete Task State Store
[**get_task_state_store**](TaskStateStoreApi.md#get_task_state_store) | **GET** /api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/state-store/{key} | Get Task State Store
[**list_task_state_store**](TaskStateStoreApi.md#list_task_state_store) | **GET** /api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/state-store | List Task State Store
[**patch_task_state_store**](TaskStateStoreApi.md#patch_task_state_store) | **PATCH** /api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/state-store/{key} | Patch Task State Store
[**set_task_state_store**](TaskStateStoreApi.md#set_task_state_store) | **PUT** /api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/state-store/{key} | Set Task State Store


# **clear_task_state_store**
> clear_task_state_store(dag_id, dag_run_id, task_id, map_index=map_index, all_map_indices=all_map_indices)

Clear Task State Store

Delete all task state store keys for a task instance.

When ``all_map_indices=true``, state store is cleared for every map index of the task and
the ``map_index`` parameter is ignored.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

```python
import airflow_client.client
from airflow_client.client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = airflow_client.client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: HTTPBearer
configuration = airflow_client.client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = airflow_client.client.TaskStateStoreApi(api_client)
    dag_id = 'dag_id_example' # str | 
    dag_run_id = 'dag_run_id_example' # str | 
    task_id = 'task_id_example' # str | 
    map_index = -1 # int |  (optional) (default to -1)
    all_map_indices = False # bool |  (optional) (default to False)

    try:
        # Clear Task State Store
        api_instance.clear_task_state_store(dag_id, dag_run_id, task_id, map_index=map_index, all_map_indices=all_map_indices)
    except Exception as e:
        print("Exception when calling TaskStateStoreApi->clear_task_state_store: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **dag_run_id** | **str**|  | 
 **task_id** | **str**|  | 
 **map_index** | **int**|  | [optional] [default to -1]
 **all_map_indices** | **bool**|  | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_task_state_store**
> delete_task_state_store(dag_id, dag_run_id, task_id, key, map_index=map_index)

Delete Task State Store

Delete a single task state store key. No-op if the key does not exist.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

```python
import airflow_client.client
from airflow_client.client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = airflow_client.client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: HTTPBearer
configuration = airflow_client.client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = airflow_client.client.TaskStateStoreApi(api_client)
    dag_id = 'dag_id_example' # str | 
    dag_run_id = 'dag_run_id_example' # str | 
    task_id = 'task_id_example' # str | 
    key = 'key_example' # str | 
    map_index = -1 # int |  (optional) (default to -1)

    try:
        # Delete Task State Store
        api_instance.delete_task_state_store(dag_id, dag_run_id, task_id, key, map_index=map_index)
    except Exception as e:
        print("Exception when calling TaskStateStoreApi->delete_task_state_store: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **dag_run_id** | **str**|  | 
 **task_id** | **str**|  | 
 **key** | **str**|  | 
 **map_index** | **int**|  | [optional] [default to -1]

### Return type

void (empty response body)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_state_store**
> TaskStateStoreResponse get_task_state_store(dag_id, dag_run_id, task_id, key, map_index=map_index)

Get Task State Store

Get a single task state store entry.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

```python
import airflow_client.client
from airflow_client.client.models.task_state_store_response import TaskStateStoreResponse
from airflow_client.client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = airflow_client.client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: HTTPBearer
configuration = airflow_client.client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = airflow_client.client.TaskStateStoreApi(api_client)
    dag_id = 'dag_id_example' # str | 
    dag_run_id = 'dag_run_id_example' # str | 
    task_id = 'task_id_example' # str | 
    key = 'key_example' # str | 
    map_index = -1 # int |  (optional) (default to -1)

    try:
        # Get Task State Store
        api_response = api_instance.get_task_state_store(dag_id, dag_run_id, task_id, key, map_index=map_index)
        print("The response of TaskStateStoreApi->get_task_state_store:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskStateStoreApi->get_task_state_store: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **dag_run_id** | **str**|  | 
 **task_id** | **str**|  | 
 **key** | **str**|  | 
 **map_index** | **int**|  | [optional] [default to -1]

### Return type

[**TaskStateStoreResponse**](TaskStateStoreResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_task_state_store**
> TaskStateStoreCollectionResponse list_task_state_store(dag_id, dag_run_id, task_id, map_index=map_index, limit=limit, offset=offset)

List Task State Store

List all task state store entries for a task instance.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

```python
import airflow_client.client
from airflow_client.client.models.task_state_store_collection_response import TaskStateStoreCollectionResponse
from airflow_client.client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = airflow_client.client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: HTTPBearer
configuration = airflow_client.client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = airflow_client.client.TaskStateStoreApi(api_client)
    dag_id = 'dag_id_example' # str | 
    dag_run_id = 'dag_run_id_example' # str | 
    task_id = 'task_id_example' # str | 
    map_index = -1 # int |  (optional) (default to -1)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List Task State Store
        api_response = api_instance.list_task_state_store(dag_id, dag_run_id, task_id, map_index=map_index, limit=limit, offset=offset)
        print("The response of TaskStateStoreApi->list_task_state_store:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskStateStoreApi->list_task_state_store: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **dag_run_id** | **str**|  | 
 **task_id** | **str**|  | 
 **map_index** | **int**|  | [optional] [default to -1]
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**TaskStateStoreCollectionResponse**](TaskStateStoreCollectionResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_task_state_store**
> object patch_task_state_store(dag_id, dag_run_id, task_id, key, task_state_store_patch_body, map_index=map_index)

Patch Task State Store

Update the value of an existing task state store key.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

```python
import airflow_client.client
from airflow_client.client.models.task_state_store_patch_body import TaskStateStorePatchBody
from airflow_client.client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = airflow_client.client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: HTTPBearer
configuration = airflow_client.client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = airflow_client.client.TaskStateStoreApi(api_client)
    dag_id = 'dag_id_example' # str | 
    dag_run_id = 'dag_run_id_example' # str | 
    task_id = 'task_id_example' # str | 
    key = 'key_example' # str | 
    task_state_store_patch_body = airflow_client.client.TaskStateStorePatchBody() # TaskStateStorePatchBody | 
    map_index = -1 # int |  (optional) (default to -1)

    try:
        # Patch Task State Store
        api_response = api_instance.patch_task_state_store(dag_id, dag_run_id, task_id, key, task_state_store_patch_body, map_index=map_index)
        print("The response of TaskStateStoreApi->patch_task_state_store:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskStateStoreApi->patch_task_state_store: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **dag_run_id** | **str**|  | 
 **task_id** | **str**|  | 
 **key** | **str**|  | 
 **task_state_store_patch_body** | [**TaskStateStorePatchBody**](TaskStateStorePatchBody.md)|  | 
 **map_index** | **int**|  | [optional] [default to -1]

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_task_state_store**
> set_task_state_store(dag_id, dag_run_id, task_id, key, task_state_store_body, map_index=map_index)

Set Task State Store

Set a task state store value. Creates or overwrites the key.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

```python
import airflow_client.client
from airflow_client.client.models.task_state_store_body import TaskStateStoreBody
from airflow_client.client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = airflow_client.client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: HTTPBearer
configuration = airflow_client.client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = airflow_client.client.TaskStateStoreApi(api_client)
    dag_id = 'dag_id_example' # str | 
    dag_run_id = 'dag_run_id_example' # str | 
    task_id = 'task_id_example' # str | 
    key = 'key_example' # str | 
    task_state_store_body = airflow_client.client.TaskStateStoreBody() # TaskStateStoreBody | 
    map_index = -1 # int |  (optional) (default to -1)

    try:
        # Set Task State Store
        api_instance.set_task_state_store(dag_id, dag_run_id, task_id, key, task_state_store_body, map_index=map_index)
    except Exception as e:
        print("Exception when calling TaskStateStoreApi->set_task_state_store: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **dag_run_id** | **str**|  | 
 **task_id** | **str**|  | 
 **key** | **str**|  | 
 **task_state_store_body** | [**TaskStateStoreBody**](TaskStateStoreBody.md)|  | 
 **map_index** | **int**|  | [optional] [default to -1]

### Return type

void (empty response body)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

