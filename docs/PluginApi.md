# airflow_client.client.PluginApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_plugins**](PluginApi.md#get_plugins) | **GET** /api/v2/plugins | Get Plugins
[**import_errors**](PluginApi.md#import_errors) | **GET** /api/v2/plugins/importErrors | Import Errors


# **get_plugins**
> PluginCollectionResponse get_plugins(limit=limit, offset=offset)

Get Plugins

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

```python
import airflow_client.client
from airflow_client.client.models.plugin_collection_response import PluginCollectionResponse
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
    api_instance = airflow_client.client.PluginApi(api_client)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # Get Plugins
        api_response = api_instance.get_plugins(limit=limit, offset=offset)
        print("The response of PluginApi->get_plugins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginApi->get_plugins: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**PluginCollectionResponse**](PluginCollectionResponse.md)

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

# **import_errors**
> PluginImportErrorCollectionResponse import_errors()

Import Errors

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

```python
import airflow_client.client
from airflow_client.client.models.plugin_import_error_collection_response import PluginImportErrorCollectionResponse
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
    api_instance = airflow_client.client.PluginApi(api_client)

    try:
        # Import Errors
        api_response = api_instance.import_errors()
        print("The response of PluginApi->import_errors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginApi->import_errors: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PluginImportErrorCollectionResponse**](PluginImportErrorCollectionResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

