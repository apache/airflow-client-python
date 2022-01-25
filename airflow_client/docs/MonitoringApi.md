# Apache Airflow Python Client.MonitoringApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_health**](MonitoringApi.md#get_health) | **GET** /health | Get instance status
[**get_version**](MonitoringApi.md#get_version) | **GET** /version | Get version information


# **get_health**
> HealthInfo get_health()

Get instance status

Get the status of Airflow's metadatabase and scheduler. It includes info about metadatabase and last heartbeat of scheduler. 

### Example


```python
import time
import airflow_client.client
from airflow_client.client.api import monitoring_api
from airflow_client.client.model.health_info import HealthInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/api/v1"
)


# Enter a context with an instance of the API client
with client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_api.MonitoringApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get instance status
        api_response = api_instance.get_health()
        pprint(api_response)
    except client.ApiException as e:
        print("Exception when calling MonitoringApi->get_health: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**HealthInfo**](HealthInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version**
> VersionInfo get_version()

Get version information

### Example


```python
import time
import airflow_client.client
from airflow_client.client.api import monitoring_api
from airflow_client.client.model.version_info import VersionInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/api/v1"
)


# Enter a context with an instance of the API client
with client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_api.MonitoringApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get version information
        api_response = api_instance.get_version()
        pprint(api_response)
    except client.ApiException as e:
        print("Exception when calling MonitoringApi->get_version: %s\n" % e)
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
**200** | Success. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

