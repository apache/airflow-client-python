# airflow_client.client.DagSourceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dag_source**](DagSourceApi.md#get_dag_source) | **GET** /api/v2/dagSources/{dag_id} | Get Dag Source


# **get_dag_source**
> DAGSourceResponse get_dag_source(dag_id, version_number=version_number, accept=accept)

Get Dag Source

Get source code using file token.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.dag_source_response import DAGSourceResponse
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
    api_instance = airflow_client.client.DagSourceApi(api_client)
    dag_id = 'dag_id_example' # str | 
    version_number = 56 # int |  (optional)
    accept = */* # str |  (optional) (default to */*)

    try:
        # Get Dag Source
        api_response = api_instance.get_dag_source(dag_id, version_number=version_number, accept=accept)
        print("The response of DagSourceApi->get_dag_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DagSourceApi->get_dag_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **version_number** | **int**|  | [optional] 
 **accept** | **str**|  | [optional] [default to */*]

### Return type

[**DAGSourceResponse**](DAGSourceResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**406** | Not Acceptable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

