# airflow_client.client.DagStatsApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dag_stats**](DagStatsApi.md#get_dag_stats) | **GET** /dagStats | List Dag statistics


# **get_dag_stats**
> DagStatsCollectionSchema get_dag_stats(dag_ids)

List Dag statistics

### Example

* Basic Authentication (Basic):

```python
import time
import airflow_client.client
from airflow_client.client.api import dag_stats_api
from airflow_client.client.model.dag_stats_collection_schema import DagStatsCollectionSchema
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
    api_instance = dag_stats_api.DagStatsApi(api_client)
    dag_ids = "dag_ids_example" # str | One or more DAG IDs separated by commas to filter relevant Dags. 

    # example passing only required values which don't have defaults set
    try:
        # List Dag statistics
        api_response = api_instance.get_dag_stats(dag_ids)
        pprint(api_response)
    except airflow_client.client.ApiException as e:
        print("Exception when calling DagStatsApi->get_dag_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_ids** | **str**| One or more DAG IDs separated by commas to filter relevant Dags.  |

### Return type

[**DagStatsCollectionSchema**](DagStatsCollectionSchema.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

