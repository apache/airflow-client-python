# airflow_client.client.DagRunApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_dag_run**](DagRunApi.md#clear_dag_run) | **POST** /api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/clear | Clear Dag Run
[**delete_dag_run**](DagRunApi.md#delete_dag_run) | **DELETE** /api/v2/dags/{dag_id}/dagRuns/{dag_run_id} | Delete Dag Run
[**get_dag_run**](DagRunApi.md#get_dag_run) | **GET** /api/v2/dags/{dag_id}/dagRuns/{dag_run_id} | Get Dag Run
[**get_dag_runs**](DagRunApi.md#get_dag_runs) | **GET** /api/v2/dags/{dag_id}/dagRuns | Get Dag Runs
[**get_list_dag_runs_batch**](DagRunApi.md#get_list_dag_runs_batch) | **POST** /api/v2/dags/{dag_id}/dagRuns/list | Get List Dag Runs Batch
[**get_upstream_asset_events**](DagRunApi.md#get_upstream_asset_events) | **GET** /api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/upstreamAssetEvents | Get Upstream Asset Events
[**patch_dag_run**](DagRunApi.md#patch_dag_run) | **PATCH** /api/v2/dags/{dag_id}/dagRuns/{dag_run_id} | Patch Dag Run
[**trigger_dag_run**](DagRunApi.md#trigger_dag_run) | **POST** /api/v2/dags/{dag_id}/dagRuns | Trigger Dag Run


# **clear_dag_run**
> ResponseClearDagRun clear_dag_run(dag_id, dag_run_id, dag_run_clear_body)

Clear Dag Run

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.dag_run_clear_body import DAGRunClearBody
from airflow_client.client.models.response_clear_dag_run import ResponseClearDagRun
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
    api_instance = airflow_client.client.DagRunApi(api_client)
    dag_id = 'dag_id_example' # str | 
    dag_run_id = 'dag_run_id_example' # str | 
    dag_run_clear_body = airflow_client.client.DAGRunClearBody() # DAGRunClearBody | 

    try:
        # Clear Dag Run
        api_response = api_instance.clear_dag_run(dag_id, dag_run_id, dag_run_clear_body)
        print("The response of DagRunApi->clear_dag_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DagRunApi->clear_dag_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **dag_run_id** | **str**|  | 
 **dag_run_clear_body** | [**DAGRunClearBody**](DAGRunClearBody.md)|  | 

### Return type

[**ResponseClearDagRun**](ResponseClearDagRun.md)

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

# **delete_dag_run**
> delete_dag_run(dag_id, dag_run_id)

Delete Dag Run

Delete a DAG Run entry.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

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

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = airflow_client.client.DagRunApi(api_client)
    dag_id = 'dag_id_example' # str | 
    dag_run_id = 'dag_run_id_example' # str | 

    try:
        # Delete Dag Run
        api_instance.delete_dag_run(dag_id, dag_run_id)
    except Exception as e:
        print("Exception when calling DagRunApi->delete_dag_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **dag_run_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dag_run**
> DAGRunResponse get_dag_run(dag_id, dag_run_id)

Get Dag Run

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.dag_run_response import DAGRunResponse
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
    api_instance = airflow_client.client.DagRunApi(api_client)
    dag_id = 'dag_id_example' # str | 
    dag_run_id = 'dag_run_id_example' # str | 

    try:
        # Get Dag Run
        api_response = api_instance.get_dag_run(dag_id, dag_run_id)
        print("The response of DagRunApi->get_dag_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DagRunApi->get_dag_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **dag_run_id** | **str**|  | 

### Return type

[**DAGRunResponse**](DAGRunResponse.md)

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

# **get_dag_runs**
> DAGRunCollectionResponse get_dag_runs(dag_id, limit=limit, offset=offset, run_after_gte=run_after_gte, run_after_lte=run_after_lte, logical_date_gte=logical_date_gte, logical_date_lte=logical_date_lte, start_date_gte=start_date_gte, start_date_lte=start_date_lte, end_date_gte=end_date_gte, end_date_lte=end_date_lte, updated_at_gte=updated_at_gte, updated_at_lte=updated_at_lte, run_type=run_type, state=state, order_by=order_by)

Get Dag Runs

Get all DAG Runs.

This endpoint allows specifying `~` as the dag_id to retrieve Dag Runs for all DAGs.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.dag_run_collection_response import DAGRunCollectionResponse
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
    api_instance = airflow_client.client.DagRunApi(api_client)
    dag_id = 'dag_id_example' # str | 
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)
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
    run_type = ['run_type_example'] # List[str] |  (optional)
    state = ['state_example'] # List[str] |  (optional)
    order_by = 'id' # str |  (optional) (default to 'id')

    try:
        # Get Dag Runs
        api_response = api_instance.get_dag_runs(dag_id, limit=limit, offset=offset, run_after_gte=run_after_gte, run_after_lte=run_after_lte, logical_date_gte=logical_date_gte, logical_date_lte=logical_date_lte, start_date_gte=start_date_gte, start_date_lte=start_date_lte, end_date_gte=end_date_gte, end_date_lte=end_date_lte, updated_at_gte=updated_at_gte, updated_at_lte=updated_at_lte, run_type=run_type, state=state, order_by=order_by)
        print("The response of DagRunApi->get_dag_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DagRunApi->get_dag_runs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
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
 **run_type** | [**List[str]**](str.md)|  | [optional] 
 **state** | [**List[str]**](str.md)|  | [optional] 
 **order_by** | **str**|  | [optional] [default to &#39;id&#39;]

### Return type

[**DAGRunCollectionResponse**](DAGRunCollectionResponse.md)

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

# **get_list_dag_runs_batch**
> DAGRunCollectionResponse get_list_dag_runs_batch(dag_id, dag_runs_batch_body)

Get List Dag Runs Batch

Get a list of DAG Runs.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.dag_run_collection_response import DAGRunCollectionResponse
from airflow_client.client.models.dag_runs_batch_body import DAGRunsBatchBody
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
    api_instance = airflow_client.client.DagRunApi(api_client)
    dag_id = 'dag_id_example' # str | 
    dag_runs_batch_body = airflow_client.client.DAGRunsBatchBody() # DAGRunsBatchBody | 

    try:
        # Get List Dag Runs Batch
        api_response = api_instance.get_list_dag_runs_batch(dag_id, dag_runs_batch_body)
        print("The response of DagRunApi->get_list_dag_runs_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DagRunApi->get_list_dag_runs_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **dag_runs_batch_body** | [**DAGRunsBatchBody**](DAGRunsBatchBody.md)|  | 

### Return type

[**DAGRunCollectionResponse**](DAGRunCollectionResponse.md)

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

# **get_upstream_asset_events**
> AssetEventCollectionResponse get_upstream_asset_events(dag_id, dag_run_id)

Get Upstream Asset Events

If dag run is asset-triggered, return the asset events that triggered it.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.asset_event_collection_response import AssetEventCollectionResponse
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
    api_instance = airflow_client.client.DagRunApi(api_client)
    dag_id = 'dag_id_example' # str | 
    dag_run_id = 'dag_run_id_example' # str | 

    try:
        # Get Upstream Asset Events
        api_response = api_instance.get_upstream_asset_events(dag_id, dag_run_id)
        print("The response of DagRunApi->get_upstream_asset_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DagRunApi->get_upstream_asset_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **dag_run_id** | **str**|  | 

### Return type

[**AssetEventCollectionResponse**](AssetEventCollectionResponse.md)

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

# **patch_dag_run**
> DAGRunResponse patch_dag_run(dag_id, dag_run_id, dag_run_patch_body, update_mask=update_mask)

Patch Dag Run

Modify a DAG Run.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.dag_run_patch_body import DAGRunPatchBody
from airflow_client.client.models.dag_run_response import DAGRunResponse
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
    api_instance = airflow_client.client.DagRunApi(api_client)
    dag_id = 'dag_id_example' # str | 
    dag_run_id = 'dag_run_id_example' # str | 
    dag_run_patch_body = airflow_client.client.DAGRunPatchBody() # DAGRunPatchBody | 
    update_mask = ['update_mask_example'] # List[str] |  (optional)

    try:
        # Patch Dag Run
        api_response = api_instance.patch_dag_run(dag_id, dag_run_id, dag_run_patch_body, update_mask=update_mask)
        print("The response of DagRunApi->patch_dag_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DagRunApi->patch_dag_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **dag_run_id** | **str**|  | 
 **dag_run_patch_body** | [**DAGRunPatchBody**](DAGRunPatchBody.md)|  | 
 **update_mask** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**DAGRunResponse**](DAGRunResponse.md)

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

# **trigger_dag_run**
> DAGRunResponse trigger_dag_run(dag_id, trigger_dag_run_post_body)

Trigger Dag Run

Trigger a DAG.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.dag_run_response import DAGRunResponse
from airflow_client.client.models.trigger_dag_run_post_body import TriggerDAGRunPostBody
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
    api_instance = airflow_client.client.DagRunApi(api_client)
    dag_id = None # object | 
    trigger_dag_run_post_body = airflow_client.client.TriggerDAGRunPostBody() # TriggerDAGRunPostBody | 

    try:
        # Trigger Dag Run
        api_response = api_instance.trigger_dag_run(dag_id, trigger_dag_run_post_body)
        print("The response of DagRunApi->trigger_dag_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DagRunApi->trigger_dag_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | [**object**](.md)|  | 
 **trigger_dag_run_post_body** | [**TriggerDAGRunPostBody**](TriggerDAGRunPostBody.md)|  | 

### Return type

[**DAGRunResponse**](DAGRunResponse.md)

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

