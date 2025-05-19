# airflow_client.client.DagVersionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dag_version**](DagVersionApi.md#get_dag_version) | **GET** /api/v2/dags/{dag_id}/dagVersions/{version_number} | Get Dag Version
[**get_dag_versions**](DagVersionApi.md#get_dag_versions) | **GET** /api/v2/dags/{dag_id}/dagVersions | Get Dag Versions


# **get_dag_version**
> DagVersionResponse get_dag_version(dag_id, version_number)

Get Dag Version

Get one Dag Version.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.dag_version_response import DagVersionResponse
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
    api_instance = airflow_client.client.DagVersionApi(api_client)
    dag_id = 'dag_id_example' # str | 
    version_number = 56 # int | 

    try:
        # Get Dag Version
        api_response = api_instance.get_dag_version(dag_id, version_number)
        print("The response of DagVersionApi->get_dag_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DagVersionApi->get_dag_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **version_number** | **int**|  | 

### Return type

[**DagVersionResponse**](DagVersionResponse.md)

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

# **get_dag_versions**
> DAGVersionCollectionResponse get_dag_versions(dag_id, limit=limit, offset=offset, version_number=version_number, bundle_name=bundle_name, bundle_version=bundle_version, order_by=order_by)

Get Dag Versions

Get all DAG Versions.

This endpoint allows specifying `~` as the dag_id to retrieve DAG Versions for all DAGs.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.dag_version_collection_response import DAGVersionCollectionResponse
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
    api_instance = airflow_client.client.DagVersionApi(api_client)
    dag_id = 'dag_id_example' # str | 
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)
    version_number = 56 # int |  (optional)
    bundle_name = 'bundle_name_example' # str |  (optional)
    bundle_version = 'bundle_version_example' # str |  (optional)
    order_by = 'id' # str |  (optional) (default to 'id')

    try:
        # Get Dag Versions
        api_response = api_instance.get_dag_versions(dag_id, limit=limit, offset=offset, version_number=version_number, bundle_name=bundle_name, bundle_version=bundle_version, order_by=order_by)
        print("The response of DagVersionApi->get_dag_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DagVersionApi->get_dag_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **version_number** | **int**|  | [optional] 
 **bundle_name** | **str**|  | [optional] 
 **bundle_version** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] [default to &#39;id&#39;]

### Return type

[**DAGVersionCollectionResponse**](DAGVersionCollectionResponse.md)

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

