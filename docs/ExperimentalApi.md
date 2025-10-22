# airflow_client.client.ExperimentalApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wait_dag_run_until_finished**](ExperimentalApi.md#wait_dag_run_until_finished) | **GET** /api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/wait | Experimental: Wait for a dag run to complete, and return task results if requested.


# **wait_dag_run_until_finished**
> object wait_dag_run_until_finished(dag_id, dag_run_id, interval, result=result)

Experimental: Wait for a dag run to complete, and return task results if requested.

🚧 This is an experimental endpoint and may change or be removed without notice.Successful response are streamed as newline-delimited JSON (NDJSON). Each line is a JSON object representing the DAG run state.

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
    result = ['result_example'] # List[str] | Collect result XCom from task. Can be set multiple times. (optional)

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
 **result** | [**List[str]**](str.md)| Collect result XCom from task. Can be set multiple times. | [optional] 

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

