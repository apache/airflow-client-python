# airflow_client.client.XComApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_xcom_entry**](XComApi.md#create_xcom_entry) | **POST** /api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/xcomEntries | Create Xcom Entry
[**get_xcom_entries**](XComApi.md#get_xcom_entries) | **GET** /api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/xcomEntries | Get Xcom Entries
[**get_xcom_entry**](XComApi.md#get_xcom_entry) | **GET** /api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/xcomEntries/{xcom_key} | Get Xcom Entry
[**update_xcom_entry**](XComApi.md#update_xcom_entry) | **PATCH** /api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/xcomEntries/{xcom_key} | Update Xcom Entry


# **create_xcom_entry**
> XComResponseNative create_xcom_entry(dag_id, task_id, dag_run_id, x_com_create_body)

Create Xcom Entry

Create an XCom entry.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

```python
import airflow_client.client
from airflow_client.client.models.x_com_create_body import XComCreateBody
from airflow_client.client.models.x_com_response_native import XComResponseNative
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
    api_instance = airflow_client.client.XComApi(api_client)
    dag_id = 'dag_id_example' # str | 
    task_id = 'task_id_example' # str | 
    dag_run_id = 'dag_run_id_example' # str | 
    x_com_create_body = airflow_client.client.XComCreateBody() # XComCreateBody | 

    try:
        # Create Xcom Entry
        api_response = api_instance.create_xcom_entry(dag_id, task_id, dag_run_id, x_com_create_body)
        print("The response of XComApi->create_xcom_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling XComApi->create_xcom_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **task_id** | **str**|  | 
 **dag_run_id** | **str**|  | 
 **x_com_create_body** | [**XComCreateBody**](XComCreateBody.md)|  | 

### Return type

[**XComResponseNative**](XComResponseNative.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_xcom_entries**
> XComCollectionResponse get_xcom_entries(dag_id, dag_run_id, task_id, xcom_key=xcom_key, map_index=map_index, limit=limit, offset=offset, xcom_key_pattern=xcom_key_pattern, dag_display_name_pattern=dag_display_name_pattern, run_id_pattern=run_id_pattern, task_id_pattern=task_id_pattern, map_index_filter=map_index_filter, logical_date_gte=logical_date_gte, logical_date_gt=logical_date_gt, logical_date_lte=logical_date_lte, logical_date_lt=logical_date_lt, run_after_gte=run_after_gte, run_after_gt=run_after_gt, run_after_lte=run_after_lte, run_after_lt=run_after_lt)

Get Xcom Entries

Get all XCom entries.

This endpoint allows specifying `~` as the dag_id, dag_run_id, task_id to retrieve XCom entries for all DAGs.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

```python
import airflow_client.client
from airflow_client.client.models.x_com_collection_response import XComCollectionResponse
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
    api_instance = airflow_client.client.XComApi(api_client)
    dag_id = 'dag_id_example' # str | 
    dag_run_id = 'dag_run_id_example' # str | 
    task_id = 'task_id_example' # str | 
    xcom_key = 'xcom_key_example' # str |  (optional)
    map_index = 56 # int |  (optional)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)
    xcom_key_pattern = 'xcom_key_pattern_example' # str | SQL LIKE expression — use `%` / `_` wildcards (e.g. `%customer_%`). Regular expressions are **not** supported. (optional)
    dag_display_name_pattern = 'dag_display_name_pattern_example' # str | SQL LIKE expression — use `%` / `_` wildcards (e.g. `%customer_%`). Regular expressions are **not** supported. (optional)
    run_id_pattern = 'run_id_pattern_example' # str | SQL LIKE expression — use `%` / `_` wildcards (e.g. `%customer_%`). Regular expressions are **not** supported. (optional)
    task_id_pattern = 'task_id_pattern_example' # str | SQL LIKE expression — use `%` / `_` wildcards (e.g. `%customer_%`). Regular expressions are **not** supported. (optional)
    map_index_filter = 56 # int |  (optional)
    logical_date_gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    logical_date_gt = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    logical_date_lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    logical_date_lt = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    run_after_gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    run_after_gt = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    run_after_lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    run_after_lt = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Get Xcom Entries
        api_response = api_instance.get_xcom_entries(dag_id, dag_run_id, task_id, xcom_key=xcom_key, map_index=map_index, limit=limit, offset=offset, xcom_key_pattern=xcom_key_pattern, dag_display_name_pattern=dag_display_name_pattern, run_id_pattern=run_id_pattern, task_id_pattern=task_id_pattern, map_index_filter=map_index_filter, logical_date_gte=logical_date_gte, logical_date_gt=logical_date_gt, logical_date_lte=logical_date_lte, logical_date_lt=logical_date_lt, run_after_gte=run_after_gte, run_after_gt=run_after_gt, run_after_lte=run_after_lte, run_after_lt=run_after_lt)
        print("The response of XComApi->get_xcom_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling XComApi->get_xcom_entries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **dag_run_id** | **str**|  | 
 **task_id** | **str**|  | 
 **xcom_key** | **str**|  | [optional] 
 **map_index** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **xcom_key_pattern** | **str**| SQL LIKE expression — use &#x60;%&#x60; / &#x60;_&#x60; wildcards (e.g. &#x60;%customer_%&#x60;). Regular expressions are **not** supported. | [optional] 
 **dag_display_name_pattern** | **str**| SQL LIKE expression — use &#x60;%&#x60; / &#x60;_&#x60; wildcards (e.g. &#x60;%customer_%&#x60;). Regular expressions are **not** supported. | [optional] 
 **run_id_pattern** | **str**| SQL LIKE expression — use &#x60;%&#x60; / &#x60;_&#x60; wildcards (e.g. &#x60;%customer_%&#x60;). Regular expressions are **not** supported. | [optional] 
 **task_id_pattern** | **str**| SQL LIKE expression — use &#x60;%&#x60; / &#x60;_&#x60; wildcards (e.g. &#x60;%customer_%&#x60;). Regular expressions are **not** supported. | [optional] 
 **map_index_filter** | **int**|  | [optional] 
 **logical_date_gte** | **datetime**|  | [optional] 
 **logical_date_gt** | **datetime**|  | [optional] 
 **logical_date_lte** | **datetime**|  | [optional] 
 **logical_date_lt** | **datetime**|  | [optional] 
 **run_after_gte** | **datetime**|  | [optional] 
 **run_after_gt** | **datetime**|  | [optional] 
 **run_after_lte** | **datetime**|  | [optional] 
 **run_after_lt** | **datetime**|  | [optional] 

### Return type

[**XComCollectionResponse**](XComCollectionResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **get_xcom_entry**
> ResponseGetXcomEntry get_xcom_entry(dag_id, task_id, dag_run_id, xcom_key, map_index=map_index, deserialize=deserialize, stringify=stringify)

Get Xcom Entry

Get an XCom entry.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

```python
import airflow_client.client
from airflow_client.client.models.response_get_xcom_entry import ResponseGetXcomEntry
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
    api_instance = airflow_client.client.XComApi(api_client)
    dag_id = 'dag_id_example' # str | 
    task_id = 'task_id_example' # str | 
    dag_run_id = 'dag_run_id_example' # str | 
    xcom_key = 'xcom_key_example' # str | 
    map_index = -1 # int |  (optional) (default to -1)
    deserialize = False # bool |  (optional) (default to False)
    stringify = False # bool |  (optional) (default to False)

    try:
        # Get Xcom Entry
        api_response = api_instance.get_xcom_entry(dag_id, task_id, dag_run_id, xcom_key, map_index=map_index, deserialize=deserialize, stringify=stringify)
        print("The response of XComApi->get_xcom_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling XComApi->get_xcom_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **task_id** | **str**|  | 
 **dag_run_id** | **str**|  | 
 **xcom_key** | **str**|  | 
 **map_index** | **int**|  | [optional] [default to -1]
 **deserialize** | **bool**|  | [optional] [default to False]
 **stringify** | **bool**|  | [optional] [default to False]

### Return type

[**ResponseGetXcomEntry**](ResponseGetXcomEntry.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **update_xcom_entry**
> XComResponseNative update_xcom_entry(dag_id, task_id, dag_run_id, xcom_key, x_com_update_body)

Update Xcom Entry

Update an existing XCom entry.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

```python
import airflow_client.client
from airflow_client.client.models.x_com_response_native import XComResponseNative
from airflow_client.client.models.x_com_update_body import XComUpdateBody
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
    api_instance = airflow_client.client.XComApi(api_client)
    dag_id = 'dag_id_example' # str | 
    task_id = 'task_id_example' # str | 
    dag_run_id = 'dag_run_id_example' # str | 
    xcom_key = 'xcom_key_example' # str | 
    x_com_update_body = airflow_client.client.XComUpdateBody() # XComUpdateBody | 

    try:
        # Update Xcom Entry
        api_response = api_instance.update_xcom_entry(dag_id, task_id, dag_run_id, xcom_key, x_com_update_body)
        print("The response of XComApi->update_xcom_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling XComApi->update_xcom_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **task_id** | **str**|  | 
 **dag_run_id** | **str**|  | 
 **xcom_key** | **str**|  | 
 **x_com_update_body** | [**XComUpdateBody**](XComUpdateBody.md)|  | 

### Return type

[**XComResponseNative**](XComResponseNative.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [HTTPBearer](../README.md#HTTPBearer)

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

