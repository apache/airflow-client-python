# airflow_client.client.ExperimentalApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dag_version_diff**](ExperimentalApi.md#get_dag_version_diff) | **GET** /api/v2/dags/{dag_id}/dagVersions/diff | Experimental: Compare what two stored versions of a Dag currently hold.
[**wait_dag_run_until_finished**](ExperimentalApi.md#wait_dag_run_until_finished) | **GET** /api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/wait | Experimental: Wait for a dag run to complete, and return task results if requested.


# **get_dag_version_diff**
> DagVersionDiffResponse get_dag_version_diff(dag_id, base_version_number, target_version_number, max_changes=max_changes)

Experimental: Compare what two stored versions of a Dag currently hold.

🚧 This is an experimental endpoint and may change or be removed without notice.

Reports observed state — what the two stored versions currently hold — not why a version was created. Version access returns the changed structure with identifying path components masked; the raw values behind those changes, and the paths that name them, are disclosed only to a caller who may also read the Dag's code.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

```python
import airflow_client.client
from airflow_client.client.models.dag_version_diff_response import DagVersionDiffResponse
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
    api_instance = airflow_client.client.ExperimentalApi(api_client)
    dag_id = 'dag_id_example' # str | 
    base_version_number = 56 # int | Version to compare from.
    target_version_number = 56 # int | Version to compare to.
    max_changes = 500 # int | Largest number of records `changes` may hold. A repeat of a path already recorded does not count towards it, and `truncated` says whether the bound dropped anything. (optional) (default to 500)

    try:
        # Experimental: Compare what two stored versions of a Dag currently hold.
        api_response = api_instance.get_dag_version_diff(dag_id, base_version_number, target_version_number, max_changes=max_changes)
        print("The response of ExperimentalApi->get_dag_version_diff:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperimentalApi->get_dag_version_diff: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **base_version_number** | **int**| Version to compare from. | 
 **target_version_number** | **int**| Version to compare to. | 
 **max_changes** | **int**| Largest number of records &#x60;changes&#x60; may hold. A repeat of a path already recorded does not count towards it, and &#x60;truncated&#x60; says whether the bound dropped anything. | [optional] [default to 500]

### Return type

[**DagVersionDiffResponse**](DagVersionDiffResponse.md)

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

# **wait_dag_run_until_finished**
> object wait_dag_run_until_finished(dag_id, dag_run_id, interval, result=result)

Experimental: Wait for a dag run to complete, and return task results if requested.

🚧 This is an experimental endpoint and may change or be removed without notice.Successful response are streamed as newline-delimited JSON (NDJSON). Each line is a JSON object representing the Dag run state.

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
    api_instance = airflow_client.client.ExperimentalApi(api_client)
    dag_id = 'dag_id_example' # str | 
    dag_run_id = 'dag_run_id_example' # str | 
    interval = 3.4 # float | Seconds to wait between dag run state checks
    result = ['result_example'] # List[str] | Collect result XCom from task. Can be set multiple times. If unset, return value of the return task as specified in the dag (in present) is returned by default. (optional)

    try:
        # Experimental: Wait for a dag run to complete, and return task results if requested.
        api_response = api_instance.wait_dag_run_until_finished(dag_id, dag_run_id, interval, result=result)
        print("The response of ExperimentalApi->wait_dag_run_until_finished:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperimentalApi->wait_dag_run_until_finished: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **dag_run_id** | **str**|  | 
 **interval** | **float**| Seconds to wait between dag run state checks | 
 **result** | [**List[str]**](str.md)| Collect result XCom from task. Can be set multiple times. If unset, return value of the return task as specified in the dag (in present) is returned by default. | [optional] 

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-ndjson

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

