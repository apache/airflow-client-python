# airflow_client.client.DagStatsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dag_stats**](DagStatsApi.md#get_dag_stats) | **GET** /api/v2/dagStats | Get Dag Stats


# **get_dag_stats**
> DagStatsCollectionResponse get_dag_stats(dag_ids=dag_ids)

Get Dag Stats

Get Dag statistics.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.dag_stats_collection_response import DagStatsCollectionResponse
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
    api_instance = airflow_client.client.DagStatsApi(api_client)
    dag_ids = ['dag_ids_example'] # List[str] |  (optional)

    try:
        # Get Dag Stats
        api_response = api_instance.get_dag_stats(dag_ids=dag_ids)
        print("The response of DagStatsApi->get_dag_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DagStatsApi->get_dag_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_ids** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**DagStatsCollectionResponse**](DagStatsCollectionResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

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

