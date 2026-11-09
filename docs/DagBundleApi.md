# airflow_client.client.DagBundleApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dag_bundle**](DagBundleApi.md#get_dag_bundle) | **GET** /api/v2/dagBundles/{bundle_name} | Get Dag Bundle
[**get_dag_bundle_files**](DagBundleApi.md#get_dag_bundle_files) | **GET** /api/v2/dagBundles/{bundle_name}/files | Get Dag Bundle Files
[**get_dag_bundles**](DagBundleApi.md#get_dag_bundles) | **GET** /api/v2/dagBundles | Get Dag Bundles


# **get_dag_bundle**
> DagBundleDetailResponse get_dag_bundle(bundle_name)

Get Dag Bundle

Get a Dag bundle.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

```python
import airflow_client.client
from airflow_client.client.models.dag_bundle_detail_response import DagBundleDetailResponse
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
    api_instance = airflow_client.client.DagBundleApi(api_client)
    bundle_name = 'bundle_name_example' # str | 

    try:
        # Get Dag Bundle
        api_response = api_instance.get_dag_bundle(bundle_name)
        print("The response of DagBundleApi->get_dag_bundle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DagBundleApi->get_dag_bundle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_name** | **str**|  | 

### Return type

[**DagBundleDetailResponse**](DagBundleDetailResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [HTTPBearer](../README.md#HTTPBearer)

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

# **get_dag_bundle_files**
> DagBundleFileCollectionResponse get_dag_bundle_files(bundle_name, limit=limit, offset=offset)

Get Dag Bundle Files

List the files in a Dag bundle, ordered by path.

A file is listed when the caller can read at least one Dag it defines. A file that recorded an
import error without registering any Dag is listed too, on the same admin-by-default terms as
``GET /importErrors`` -- a file that fails before defining a Dag has no Dag to authorize on,
and it is the case this page most needs to show.

``dag_count`` counts live Dags only. Dag rows are never deleted: a file that fails to import
has every Dag in it marked stale, and so does a file dropped from the bundle. A file therefore
stays listed on the strength of a live Dag *or* an import error, so a file that has just broken
does not vanish from the page someone opened to find out why, while a file deleted long ago
drops out instead of lingering forever.

Parse times come from the Dags in the file rather than the file itself, which is the only
record Airflow keeps: a file whose every Dag was removed keeps no parse time of its own.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

```python
import airflow_client.client
from airflow_client.client.models.dag_bundle_file_collection_response import DagBundleFileCollectionResponse
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
    api_instance = airflow_client.client.DagBundleApi(api_client)
    bundle_name = 'bundle_name_example' # str | 
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # Get Dag Bundle Files
        api_response = api_instance.get_dag_bundle_files(bundle_name, limit=limit, offset=offset)
        print("The response of DagBundleApi->get_dag_bundle_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DagBundleApi->get_dag_bundle_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_name** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**DagBundleFileCollectionResponse**](DagBundleFileCollectionResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [HTTPBearer](../README.md#HTTPBearer)

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

# **get_dag_bundles**
> DagBundleCollectionResponse get_dag_bundles(limit=limit, offset=offset, order_by=order_by)

Get Dag Bundles

List the Dag bundles Airflow knows about.

Reports the version of each bundle Airflow currently holds and when a Dag processor last
refreshed it, so whoever deployed the code can tell whether it has been picked up yet.

A bundle is visible to a user who can read at least one Dag recorded against it. A bundle
holding no registered Dag at all has nothing to authorize against, so it is listed only for a
user holding the admin-by-default ``AccessView.IMPORT_ERRORS_ALL`` for that bundle's team --
the same view, scoped the same way, that governs import errors for a file that never
registered a Dag.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

```python
import airflow_client.client
from airflow_client.client.models.dag_bundle_collection_response import DagBundleCollectionResponse
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
    api_instance = airflow_client.client.DagBundleApi(api_client)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)
    order_by = ["name"] # List[str] | Attributes to order by, multi criteria sort is supported. Prefix with `-` for descending order. Supported attributes: `name, version, last_refreshed, active` (optional) (default to ["name"])

    try:
        # Get Dag Bundles
        api_response = api_instance.get_dag_bundles(limit=limit, offset=offset, order_by=order_by)
        print("The response of DagBundleApi->get_dag_bundles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DagBundleApi->get_dag_bundles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **order_by** | [**List[str]**](str.md)| Attributes to order by, multi criteria sort is supported. Prefix with &#x60;-&#x60; for descending order. Supported attributes: &#x60;name, version, last_refreshed, active&#x60; | [optional] [default to [&quot;name&quot;]]

### Return type

[**DagBundleCollectionResponse**](DagBundleCollectionResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [HTTPBearer](../README.md#HTTPBearer)

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

