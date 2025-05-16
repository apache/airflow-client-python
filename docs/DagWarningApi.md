# airflow_client.client.DagWarningApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_dag_warnings**](DagWarningApi.md#list_dag_warnings) | **GET** /api/v2/dagWarnings | List Dag Warnings


# **list_dag_warnings**
> DAGWarningCollectionResponse list_dag_warnings(dag_id=dag_id, warning_type=warning_type, limit=limit, offset=offset, order_by=order_by)

List Dag Warnings

Get a list of DAG warnings.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.dag_warning_collection_response import DAGWarningCollectionResponse
from airflow_client.client.models.dag_warning_type import DagWarningType
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
    api_instance = airflow_client.client.DagWarningApi(api_client)
    dag_id = 'dag_id_example' # str |  (optional)
    warning_type = airflow_client.client.DagWarningType() # DagWarningType |  (optional)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)
    order_by = 'dag_id' # str |  (optional) (default to 'dag_id')

    try:
        # List Dag Warnings
        api_response = api_instance.list_dag_warnings(dag_id=dag_id, warning_type=warning_type, limit=limit, offset=offset, order_by=order_by)
        print("The response of DagWarningApi->list_dag_warnings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DagWarningApi->list_dag_warnings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | [optional] 
 **warning_type** | [**DagWarningType**](.md)|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **order_by** | **str**|  | [optional] [default to &#39;dag_id&#39;]

### Return type

[**DAGWarningCollectionResponse**](DAGWarningCollectionResponse.md)

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

