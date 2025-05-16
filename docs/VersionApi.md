# airflow_client.client.VersionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_version**](VersionApi.md#get_version) | **GET** /api/v2/version | Get Version


# **get_version**
> VersionInfo get_version()

Get Version

Get version information.

### Example


```python
import airflow_client.client
from airflow_client.client.models.version_info import VersionInfo
from airflow_client.client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = airflow_client.client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = airflow_client.client.VersionApi(api_client)

    try:
        # Get Version
        api_response = api_instance.get_version()
        print("The response of VersionApi->get_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionApi->get_version: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**VersionInfo**](VersionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

