# airflow_client.client.TaskInstanceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_extra_links**](TaskInstanceApi.md#get_extra_links) | **GET** /api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/links | Get Extra Links
[**get_log**](TaskInstanceApi.md#get_log) | **GET** /api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/logs/{try_number} | Get Log
[**get_mapped_task_instance**](TaskInstanceApi.md#get_mapped_task_instance) | **GET** /api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/{map_index} | Get Mapped Task Instance
[**get_mapped_task_instance_tries**](TaskInstanceApi.md#get_mapped_task_instance_tries) | **GET** /api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/{map_index}/tries | Get Mapped Task Instance Tries
[**get_mapped_task_instance_try_details**](TaskInstanceApi.md#get_mapped_task_instance_try_details) | **GET** /api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/{map_index}/tries/{task_try_number} | Get Mapped Task Instance Try Details
[**get_mapped_task_instances**](TaskInstanceApi.md#get_mapped_task_instances) | **GET** /api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/listMapped | Get Mapped Task Instances
[**get_task_instance**](TaskInstanceApi.md#get_task_instance) | **GET** /api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id} | Get Task Instance
[**get_task_instance_dependencies**](TaskInstanceApi.md#get_task_instance_dependencies) | **GET** /api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/dependencies | Get Task Instance Dependencies
[**get_task_instance_dependencies_by_map_index**](TaskInstanceApi.md#get_task_instance_dependencies_by_map_index) | **GET** /api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/{map_index}/dependencies | Get Task Instance Dependencies
[**get_task_instance_tries**](TaskInstanceApi.md#get_task_instance_tries) | **GET** /api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/tries | Get Task Instance Tries
[**get_task_instance_try_details**](TaskInstanceApi.md#get_task_instance_try_details) | **GET** /api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/tries/{task_try_number} | Get Task Instance Try Details
[**get_task_instances**](TaskInstanceApi.md#get_task_instances) | **GET** /api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances | Get Task Instances
[**get_task_instances_batch**](TaskInstanceApi.md#get_task_instances_batch) | **POST** /api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/list | Get Task Instances Batch
[**patch_task_instance**](TaskInstanceApi.md#patch_task_instance) | **PATCH** /api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id} | Patch Task Instance
[**patch_task_instance_by_map_index**](TaskInstanceApi.md#patch_task_instance_by_map_index) | **PATCH** /api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/{map_index} | Patch Task Instance
[**patch_task_instance_dry_run**](TaskInstanceApi.md#patch_task_instance_dry_run) | **PATCH** /api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/dry_run | Patch Task Instance Dry Run
[**patch_task_instance_dry_run_by_map_index**](TaskInstanceApi.md#patch_task_instance_dry_run_by_map_index) | **PATCH** /api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/{map_index}/dry_run | Patch Task Instance Dry Run
[**post_clear_task_instances**](TaskInstanceApi.md#post_clear_task_instances) | **POST** /api/v2/dags/{dag_id}/clearTaskInstances | Post Clear Task Instances


# **get_extra_links**
> ExtraLinkCollectionResponse get_extra_links(dag_id, dag_run_id, task_id, map_index=map_index)

Get Extra Links

Get extra links for task instance.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.extra_link_collection_response import ExtraLinkCollectionResponse
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

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = airflow_client.client.TaskInstanceApi(api_client)
    dag_id = 'dag_id_example' # str | 
    dag_run_id = 'dag_run_id_example' # str | 
    task_id = 'task_id_example' # str | 
    map_index = -1 # int |  (optional) (default to -1)

    try:
        # Get Extra Links
        api_response = api_instance.get_extra_links(dag_id, dag_run_id, task_id, map_index=map_index)
        print("The response of TaskInstanceApi->get_extra_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskInstanceApi->get_extra_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **dag_run_id** | **str**|  | 
 **task_id** | **str**|  | 
 **map_index** | **int**|  | [optional] [default to -1]

### Return type

[**ExtraLinkCollectionResponse**](ExtraLinkCollectionResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

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

# **get_log**
> TaskInstancesLogResponse get_log(dag_id, dag_run_id, task_id, try_number, full_content=full_content, map_index=map_index, token=token, accept=accept)

Get Log

Get logs for a specific task instance.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.task_instances_log_response import TaskInstancesLogResponse
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

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = airflow_client.client.TaskInstanceApi(api_client)
    dag_id = 'dag_id_example' # str | 
    dag_run_id = 'dag_run_id_example' # str | 
    task_id = 'task_id_example' # str | 
    try_number = 56 # int | 
    full_content = False # bool |  (optional) (default to False)
    map_index = -1 # int |  (optional) (default to -1)
    token = 'token_example' # str |  (optional)
    accept = */* # str |  (optional) (default to */*)

    try:
        # Get Log
        api_response = api_instance.get_log(dag_id, dag_run_id, task_id, try_number, full_content=full_content, map_index=map_index, token=token, accept=accept)
        print("The response of TaskInstanceApi->get_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskInstanceApi->get_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **dag_run_id** | **str**|  | 
 **task_id** | **str**|  | 
 **try_number** | **int**|  | 
 **full_content** | **bool**|  | [optional] [default to False]
 **map_index** | **int**|  | [optional] [default to -1]
 **token** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] [default to */*]

### Return type

[**TaskInstancesLogResponse**](TaskInstancesLogResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mapped_task_instance**
> TaskInstanceResponse get_mapped_task_instance(dag_id, dag_run_id, task_id, map_index)

Get Mapped Task Instance

Get task instance.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.task_instance_response import TaskInstanceResponse
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

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = airflow_client.client.TaskInstanceApi(api_client)
    dag_id = 'dag_id_example' # str | 
    dag_run_id = 'dag_run_id_example' # str | 
    task_id = 'task_id_example' # str | 
    map_index = 56 # int | 

    try:
        # Get Mapped Task Instance
        api_response = api_instance.get_mapped_task_instance(dag_id, dag_run_id, task_id, map_index)
        print("The response of TaskInstanceApi->get_mapped_task_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskInstanceApi->get_mapped_task_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **dag_run_id** | **str**|  | 
 **task_id** | **str**|  | 
 **map_index** | **int**|  | 

### Return type

[**TaskInstanceResponse**](TaskInstanceResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

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

# **get_mapped_task_instance_tries**
> TaskInstanceHistoryCollectionResponse get_mapped_task_instance_tries(dag_id, dag_run_id, task_id, map_index)

Get Mapped Task Instance Tries

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.task_instance_history_collection_response import TaskInstanceHistoryCollectionResponse
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

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = airflow_client.client.TaskInstanceApi(api_client)
    dag_id = 'dag_id_example' # str | 
    dag_run_id = 'dag_run_id_example' # str | 
    task_id = 'task_id_example' # str | 
    map_index = 56 # int | 

    try:
        # Get Mapped Task Instance Tries
        api_response = api_instance.get_mapped_task_instance_tries(dag_id, dag_run_id, task_id, map_index)
        print("The response of TaskInstanceApi->get_mapped_task_instance_tries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskInstanceApi->get_mapped_task_instance_tries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **dag_run_id** | **str**|  | 
 **task_id** | **str**|  | 
 **map_index** | **int**|  | 

### Return type

[**TaskInstanceHistoryCollectionResponse**](TaskInstanceHistoryCollectionResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

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

# **get_mapped_task_instance_try_details**
> TaskInstanceHistoryResponse get_mapped_task_instance_try_details(dag_id, dag_run_id, task_id, task_try_number, map_index)

Get Mapped Task Instance Try Details

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.task_instance_history_response import TaskInstanceHistoryResponse
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

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = airflow_client.client.TaskInstanceApi(api_client)
    dag_id = 'dag_id_example' # str | 
    dag_run_id = 'dag_run_id_example' # str | 
    task_id = 'task_id_example' # str | 
    task_try_number = 56 # int | 
    map_index = 56 # int | 

    try:
        # Get Mapped Task Instance Try Details
        api_response = api_instance.get_mapped_task_instance_try_details(dag_id, dag_run_id, task_id, task_try_number, map_index)
        print("The response of TaskInstanceApi->get_mapped_task_instance_try_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskInstanceApi->get_mapped_task_instance_try_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **dag_run_id** | **str**|  | 
 **task_id** | **str**|  | 
 **task_try_number** | **int**|  | 
 **map_index** | **int**|  | 

### Return type

[**TaskInstanceHistoryResponse**](TaskInstanceHistoryResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

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

# **get_mapped_task_instances**
> TaskInstanceCollectionResponse get_mapped_task_instances(dag_id, dag_run_id, task_id, run_after_gte=run_after_gte, run_after_lte=run_after_lte, logical_date_gte=logical_date_gte, logical_date_lte=logical_date_lte, start_date_gte=start_date_gte, start_date_lte=start_date_lte, end_date_gte=end_date_gte, end_date_lte=end_date_lte, updated_at_gte=updated_at_gte, updated_at_lte=updated_at_lte, duration_gte=duration_gte, duration_lte=duration_lte, state=state, pool=pool, queue=queue, executor=executor, version_number=version_number, limit=limit, offset=offset, order_by=order_by)

Get Mapped Task Instances

Get list of mapped task instances.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.task_instance_collection_response import TaskInstanceCollectionResponse
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

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = airflow_client.client.TaskInstanceApi(api_client)
    dag_id = 'dag_id_example' # str | 
    dag_run_id = 'dag_run_id_example' # str | 
    task_id = 'task_id_example' # str | 
    run_after_gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    run_after_lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    logical_date_gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    logical_date_lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    start_date_gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    start_date_lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date_gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date_lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    updated_at_gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    updated_at_lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    duration_gte = 3.4 # float |  (optional)
    duration_lte = 3.4 # float |  (optional)
    state = ['state_example'] # List[str] |  (optional)
    pool = ['pool_example'] # List[str] |  (optional)
    queue = ['queue_example'] # List[str] |  (optional)
    executor = ['executor_example'] # List[str] |  (optional)
    version_number = [56] # List[int] |  (optional)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)
    order_by = 'map_index' # str |  (optional) (default to 'map_index')

    try:
        # Get Mapped Task Instances
        api_response = api_instance.get_mapped_task_instances(dag_id, dag_run_id, task_id, run_after_gte=run_after_gte, run_after_lte=run_after_lte, logical_date_gte=logical_date_gte, logical_date_lte=logical_date_lte, start_date_gte=start_date_gte, start_date_lte=start_date_lte, end_date_gte=end_date_gte, end_date_lte=end_date_lte, updated_at_gte=updated_at_gte, updated_at_lte=updated_at_lte, duration_gte=duration_gte, duration_lte=duration_lte, state=state, pool=pool, queue=queue, executor=executor, version_number=version_number, limit=limit, offset=offset, order_by=order_by)
        print("The response of TaskInstanceApi->get_mapped_task_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskInstanceApi->get_mapped_task_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **dag_run_id** | **str**|  | 
 **task_id** | **str**|  | 
 **run_after_gte** | **datetime**|  | [optional] 
 **run_after_lte** | **datetime**|  | [optional] 
 **logical_date_gte** | **datetime**|  | [optional] 
 **logical_date_lte** | **datetime**|  | [optional] 
 **start_date_gte** | **datetime**|  | [optional] 
 **start_date_lte** | **datetime**|  | [optional] 
 **end_date_gte** | **datetime**|  | [optional] 
 **end_date_lte** | **datetime**|  | [optional] 
 **updated_at_gte** | **datetime**|  | [optional] 
 **updated_at_lte** | **datetime**|  | [optional] 
 **duration_gte** | **float**|  | [optional] 
 **duration_lte** | **float**|  | [optional] 
 **state** | [**List[str]**](str.md)|  | [optional] 
 **pool** | [**List[str]**](str.md)|  | [optional] 
 **queue** | [**List[str]**](str.md)|  | [optional] 
 **executor** | [**List[str]**](str.md)|  | [optional] 
 **version_number** | [**List[int]**](int.md)|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **order_by** | **str**|  | [optional] [default to &#39;map_index&#39;]

### Return type

[**TaskInstanceCollectionResponse**](TaskInstanceCollectionResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

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

# **get_task_instance**
> TaskInstanceResponse get_task_instance(dag_id, dag_run_id, task_id)

Get Task Instance

Get task instance.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.task_instance_response import TaskInstanceResponse
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

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = airflow_client.client.TaskInstanceApi(api_client)
    dag_id = 'dag_id_example' # str | 
    dag_run_id = 'dag_run_id_example' # str | 
    task_id = 'task_id_example' # str | 

    try:
        # Get Task Instance
        api_response = api_instance.get_task_instance(dag_id, dag_run_id, task_id)
        print("The response of TaskInstanceApi->get_task_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskInstanceApi->get_task_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **dag_run_id** | **str**|  | 
 **task_id** | **str**|  | 

### Return type

[**TaskInstanceResponse**](TaskInstanceResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

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

# **get_task_instance_dependencies**
> TaskDependencyCollectionResponse get_task_instance_dependencies(dag_id, dag_run_id, task_id, map_index=map_index)

Get Task Instance Dependencies

Get dependencies blocking task from getting scheduled.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.task_dependency_collection_response import TaskDependencyCollectionResponse
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

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = airflow_client.client.TaskInstanceApi(api_client)
    dag_id = 'dag_id_example' # str | 
    dag_run_id = 'dag_run_id_example' # str | 
    task_id = 'task_id_example' # str | 
    map_index = -1 # int |  (optional) (default to -1)

    try:
        # Get Task Instance Dependencies
        api_response = api_instance.get_task_instance_dependencies(dag_id, dag_run_id, task_id, map_index=map_index)
        print("The response of TaskInstanceApi->get_task_instance_dependencies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskInstanceApi->get_task_instance_dependencies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **dag_run_id** | **str**|  | 
 **task_id** | **str**|  | 
 **map_index** | **int**|  | [optional] [default to -1]

### Return type

[**TaskDependencyCollectionResponse**](TaskDependencyCollectionResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

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

# **get_task_instance_dependencies_by_map_index**
> TaskDependencyCollectionResponse get_task_instance_dependencies_by_map_index(dag_id, dag_run_id, task_id, map_index)

Get Task Instance Dependencies

Get dependencies blocking task from getting scheduled.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.task_dependency_collection_response import TaskDependencyCollectionResponse
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

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = airflow_client.client.TaskInstanceApi(api_client)
    dag_id = 'dag_id_example' # str | 
    dag_run_id = 'dag_run_id_example' # str | 
    task_id = 'task_id_example' # str | 
    map_index = 56 # int | 

    try:
        # Get Task Instance Dependencies
        api_response = api_instance.get_task_instance_dependencies_by_map_index(dag_id, dag_run_id, task_id, map_index)
        print("The response of TaskInstanceApi->get_task_instance_dependencies_by_map_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskInstanceApi->get_task_instance_dependencies_by_map_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **dag_run_id** | **str**|  | 
 **task_id** | **str**|  | 
 **map_index** | **int**|  | 

### Return type

[**TaskDependencyCollectionResponse**](TaskDependencyCollectionResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

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

# **get_task_instance_tries**
> TaskInstanceHistoryCollectionResponse get_task_instance_tries(dag_id, dag_run_id, task_id, map_index=map_index)

Get Task Instance Tries

Get list of task instances history.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.task_instance_history_collection_response import TaskInstanceHistoryCollectionResponse
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

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = airflow_client.client.TaskInstanceApi(api_client)
    dag_id = 'dag_id_example' # str | 
    dag_run_id = 'dag_run_id_example' # str | 
    task_id = 'task_id_example' # str | 
    map_index = -1 # int |  (optional) (default to -1)

    try:
        # Get Task Instance Tries
        api_response = api_instance.get_task_instance_tries(dag_id, dag_run_id, task_id, map_index=map_index)
        print("The response of TaskInstanceApi->get_task_instance_tries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskInstanceApi->get_task_instance_tries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **dag_run_id** | **str**|  | 
 **task_id** | **str**|  | 
 **map_index** | **int**|  | [optional] [default to -1]

### Return type

[**TaskInstanceHistoryCollectionResponse**](TaskInstanceHistoryCollectionResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

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

# **get_task_instance_try_details**
> TaskInstanceHistoryResponse get_task_instance_try_details(dag_id, dag_run_id, task_id, task_try_number, map_index=map_index)

Get Task Instance Try Details

Get task instance details by try number.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.task_instance_history_response import TaskInstanceHistoryResponse
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

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = airflow_client.client.TaskInstanceApi(api_client)
    dag_id = 'dag_id_example' # str | 
    dag_run_id = 'dag_run_id_example' # str | 
    task_id = 'task_id_example' # str | 
    task_try_number = 56 # int | 
    map_index = -1 # int |  (optional) (default to -1)

    try:
        # Get Task Instance Try Details
        api_response = api_instance.get_task_instance_try_details(dag_id, dag_run_id, task_id, task_try_number, map_index=map_index)
        print("The response of TaskInstanceApi->get_task_instance_try_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskInstanceApi->get_task_instance_try_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **dag_run_id** | **str**|  | 
 **task_id** | **str**|  | 
 **task_try_number** | **int**|  | 
 **map_index** | **int**|  | [optional] [default to -1]

### Return type

[**TaskInstanceHistoryResponse**](TaskInstanceHistoryResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

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

# **get_task_instances**
> TaskInstanceCollectionResponse get_task_instances(dag_id, dag_run_id, task_id=task_id, run_after_gte=run_after_gte, run_after_lte=run_after_lte, logical_date_gte=logical_date_gte, logical_date_lte=logical_date_lte, start_date_gte=start_date_gte, start_date_lte=start_date_lte, end_date_gte=end_date_gte, end_date_lte=end_date_lte, updated_at_gte=updated_at_gte, updated_at_lte=updated_at_lte, duration_gte=duration_gte, duration_lte=duration_lte, task_display_name_pattern=task_display_name_pattern, state=state, pool=pool, queue=queue, executor=executor, version_number=version_number, limit=limit, offset=offset, order_by=order_by)

Get Task Instances

Get list of task instances.

This endpoint allows specifying `~` as the dag_id, dag_run_id to retrieve Task Instances for all DAGs
and DAG runs.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.task_instance_collection_response import TaskInstanceCollectionResponse
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

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = airflow_client.client.TaskInstanceApi(api_client)
    dag_id = 'dag_id_example' # str | 
    dag_run_id = 'dag_run_id_example' # str | 
    task_id = 'task_id_example' # str |  (optional)
    run_after_gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    run_after_lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    logical_date_gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    logical_date_lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    start_date_gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    start_date_lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date_gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date_lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    updated_at_gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    updated_at_lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    duration_gte = 3.4 # float |  (optional)
    duration_lte = 3.4 # float |  (optional)
    task_display_name_pattern = 'task_display_name_pattern_example' # str |  (optional)
    state = ['state_example'] # List[str] |  (optional)
    pool = ['pool_example'] # List[str] |  (optional)
    queue = ['queue_example'] # List[str] |  (optional)
    executor = ['executor_example'] # List[str] |  (optional)
    version_number = [56] # List[int] |  (optional)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)
    order_by = 'map_index' # str |  (optional) (default to 'map_index')

    try:
        # Get Task Instances
        api_response = api_instance.get_task_instances(dag_id, dag_run_id, task_id=task_id, run_after_gte=run_after_gte, run_after_lte=run_after_lte, logical_date_gte=logical_date_gte, logical_date_lte=logical_date_lte, start_date_gte=start_date_gte, start_date_lte=start_date_lte, end_date_gte=end_date_gte, end_date_lte=end_date_lte, updated_at_gte=updated_at_gte, updated_at_lte=updated_at_lte, duration_gte=duration_gte, duration_lte=duration_lte, task_display_name_pattern=task_display_name_pattern, state=state, pool=pool, queue=queue, executor=executor, version_number=version_number, limit=limit, offset=offset, order_by=order_by)
        print("The response of TaskInstanceApi->get_task_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskInstanceApi->get_task_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **dag_run_id** | **str**|  | 
 **task_id** | **str**|  | [optional] 
 **run_after_gte** | **datetime**|  | [optional] 
 **run_after_lte** | **datetime**|  | [optional] 
 **logical_date_gte** | **datetime**|  | [optional] 
 **logical_date_lte** | **datetime**|  | [optional] 
 **start_date_gte** | **datetime**|  | [optional] 
 **start_date_lte** | **datetime**|  | [optional] 
 **end_date_gte** | **datetime**|  | [optional] 
 **end_date_lte** | **datetime**|  | [optional] 
 **updated_at_gte** | **datetime**|  | [optional] 
 **updated_at_lte** | **datetime**|  | [optional] 
 **duration_gte** | **float**|  | [optional] 
 **duration_lte** | **float**|  | [optional] 
 **task_display_name_pattern** | **str**|  | [optional] 
 **state** | [**List[str]**](str.md)|  | [optional] 
 **pool** | [**List[str]**](str.md)|  | [optional] 
 **queue** | [**List[str]**](str.md)|  | [optional] 
 **executor** | [**List[str]**](str.md)|  | [optional] 
 **version_number** | [**List[int]**](int.md)|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **order_by** | **str**|  | [optional] [default to &#39;map_index&#39;]

### Return type

[**TaskInstanceCollectionResponse**](TaskInstanceCollectionResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

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

# **get_task_instances_batch**
> TaskInstanceCollectionResponse get_task_instances_batch(dag_id, dag_run_id, task_instances_batch_body)

Get Task Instances Batch

Get list of task instances.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.task_instance_collection_response import TaskInstanceCollectionResponse
from airflow_client.client.models.task_instances_batch_body import TaskInstancesBatchBody
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

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = airflow_client.client.TaskInstanceApi(api_client)
    dag_id = 'dag_id_example' # str | 
    dag_run_id = 'dag_run_id_example' # str | 
    task_instances_batch_body = airflow_client.client.TaskInstancesBatchBody() # TaskInstancesBatchBody | 

    try:
        # Get Task Instances Batch
        api_response = api_instance.get_task_instances_batch(dag_id, dag_run_id, task_instances_batch_body)
        print("The response of TaskInstanceApi->get_task_instances_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskInstanceApi->get_task_instances_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **dag_run_id** | **str**|  | 
 **task_instances_batch_body** | [**TaskInstancesBatchBody**](TaskInstancesBatchBody.md)|  | 

### Return type

[**TaskInstanceCollectionResponse**](TaskInstanceCollectionResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

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

# **patch_task_instance**
> TaskInstanceCollectionResponse patch_task_instance(dag_id, dag_run_id, task_id, patch_task_instance_body, map_index=map_index, update_mask=update_mask)

Patch Task Instance

Update a task instance.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.patch_task_instance_body import PatchTaskInstanceBody
from airflow_client.client.models.task_instance_collection_response import TaskInstanceCollectionResponse
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

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = airflow_client.client.TaskInstanceApi(api_client)
    dag_id = 'dag_id_example' # str | 
    dag_run_id = 'dag_run_id_example' # str | 
    task_id = 'task_id_example' # str | 
    patch_task_instance_body = airflow_client.client.PatchTaskInstanceBody() # PatchTaskInstanceBody | 
    map_index = 56 # int |  (optional)
    update_mask = ['update_mask_example'] # List[str] |  (optional)

    try:
        # Patch Task Instance
        api_response = api_instance.patch_task_instance(dag_id, dag_run_id, task_id, patch_task_instance_body, map_index=map_index, update_mask=update_mask)
        print("The response of TaskInstanceApi->patch_task_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskInstanceApi->patch_task_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **dag_run_id** | **str**|  | 
 **task_id** | **str**|  | 
 **patch_task_instance_body** | [**PatchTaskInstanceBody**](PatchTaskInstanceBody.md)|  | 
 **map_index** | **int**|  | [optional] 
 **update_mask** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**TaskInstanceCollectionResponse**](TaskInstanceCollectionResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_task_instance_by_map_index**
> TaskInstanceCollectionResponse patch_task_instance_by_map_index(dag_id, dag_run_id, task_id, map_index, patch_task_instance_body, update_mask=update_mask)

Patch Task Instance

Update a task instance.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.patch_task_instance_body import PatchTaskInstanceBody
from airflow_client.client.models.task_instance_collection_response import TaskInstanceCollectionResponse
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

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = airflow_client.client.TaskInstanceApi(api_client)
    dag_id = 'dag_id_example' # str | 
    dag_run_id = 'dag_run_id_example' # str | 
    task_id = 'task_id_example' # str | 
    map_index = 56 # int | 
    patch_task_instance_body = airflow_client.client.PatchTaskInstanceBody() # PatchTaskInstanceBody | 
    update_mask = ['update_mask_example'] # List[str] |  (optional)

    try:
        # Patch Task Instance
        api_response = api_instance.patch_task_instance_by_map_index(dag_id, dag_run_id, task_id, map_index, patch_task_instance_body, update_mask=update_mask)
        print("The response of TaskInstanceApi->patch_task_instance_by_map_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskInstanceApi->patch_task_instance_by_map_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **dag_run_id** | **str**|  | 
 **task_id** | **str**|  | 
 **map_index** | **int**|  | 
 **patch_task_instance_body** | [**PatchTaskInstanceBody**](PatchTaskInstanceBody.md)|  | 
 **update_mask** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**TaskInstanceCollectionResponse**](TaskInstanceCollectionResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_task_instance_dry_run**
> TaskInstanceCollectionResponse patch_task_instance_dry_run(dag_id, dag_run_id, task_id, patch_task_instance_body, map_index=map_index, update_mask=update_mask)

Patch Task Instance Dry Run

Update a task instance dry_run mode.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.patch_task_instance_body import PatchTaskInstanceBody
from airflow_client.client.models.task_instance_collection_response import TaskInstanceCollectionResponse
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

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = airflow_client.client.TaskInstanceApi(api_client)
    dag_id = 'dag_id_example' # str | 
    dag_run_id = 'dag_run_id_example' # str | 
    task_id = 'task_id_example' # str | 
    patch_task_instance_body = airflow_client.client.PatchTaskInstanceBody() # PatchTaskInstanceBody | 
    map_index = 56 # int |  (optional)
    update_mask = ['update_mask_example'] # List[str] |  (optional)

    try:
        # Patch Task Instance Dry Run
        api_response = api_instance.patch_task_instance_dry_run(dag_id, dag_run_id, task_id, patch_task_instance_body, map_index=map_index, update_mask=update_mask)
        print("The response of TaskInstanceApi->patch_task_instance_dry_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskInstanceApi->patch_task_instance_dry_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **dag_run_id** | **str**|  | 
 **task_id** | **str**|  | 
 **patch_task_instance_body** | [**PatchTaskInstanceBody**](PatchTaskInstanceBody.md)|  | 
 **map_index** | **int**|  | [optional] 
 **update_mask** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**TaskInstanceCollectionResponse**](TaskInstanceCollectionResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_task_instance_dry_run_by_map_index**
> TaskInstanceCollectionResponse patch_task_instance_dry_run_by_map_index(dag_id, dag_run_id, task_id, map_index, patch_task_instance_body, update_mask=update_mask)

Patch Task Instance Dry Run

Update a task instance dry_run mode.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.patch_task_instance_body import PatchTaskInstanceBody
from airflow_client.client.models.task_instance_collection_response import TaskInstanceCollectionResponse
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

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = airflow_client.client.TaskInstanceApi(api_client)
    dag_id = 'dag_id_example' # str | 
    dag_run_id = 'dag_run_id_example' # str | 
    task_id = 'task_id_example' # str | 
    map_index = 56 # int | 
    patch_task_instance_body = airflow_client.client.PatchTaskInstanceBody() # PatchTaskInstanceBody | 
    update_mask = ['update_mask_example'] # List[str] |  (optional)

    try:
        # Patch Task Instance Dry Run
        api_response = api_instance.patch_task_instance_dry_run_by_map_index(dag_id, dag_run_id, task_id, map_index, patch_task_instance_body, update_mask=update_mask)
        print("The response of TaskInstanceApi->patch_task_instance_dry_run_by_map_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskInstanceApi->patch_task_instance_dry_run_by_map_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **dag_run_id** | **str**|  | 
 **task_id** | **str**|  | 
 **map_index** | **int**|  | 
 **patch_task_instance_body** | [**PatchTaskInstanceBody**](PatchTaskInstanceBody.md)|  | 
 **update_mask** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**TaskInstanceCollectionResponse**](TaskInstanceCollectionResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_clear_task_instances**
> TaskInstanceCollectionResponse post_clear_task_instances(dag_id, clear_task_instances_body)

Post Clear Task Instances

Clear task instances.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.clear_task_instances_body import ClearTaskInstancesBody
from airflow_client.client.models.task_instance_collection_response import TaskInstanceCollectionResponse
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

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = airflow_client.client.TaskInstanceApi(api_client)
    dag_id = 'dag_id_example' # str | 
    clear_task_instances_body = airflow_client.client.ClearTaskInstancesBody() # ClearTaskInstancesBody | 

    try:
        # Post Clear Task Instances
        api_response = api_instance.post_clear_task_instances(dag_id, clear_task_instances_body)
        print("The response of TaskInstanceApi->post_clear_task_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskInstanceApi->post_clear_task_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **clear_task_instances_body** | [**ClearTaskInstancesBody**](ClearTaskInstancesBody.md)|  | 

### Return type

[**TaskInstanceCollectionResponse**](TaskInstanceCollectionResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

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

