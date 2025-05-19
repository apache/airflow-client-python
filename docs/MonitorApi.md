# airflow_client.client.MonitorApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_health**](MonitorApi.md#get_health) | **GET** /api/v2/monitor/health | Get Health


# **get_health**
> HealthInfoResponse get_health()

Get Health

### Example


```python
import airflow_client.client
from airflow_client.client.models.health_info_response import HealthInfoResponse
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
    api_instance = airflow_client.client.MonitorApi(api_client)

    try:
        # Get Health
        api_response = api_instance.get_health()
        print("The response of MonitorApi->get_health:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonitorApi->get_health: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HealthInfoResponse**](HealthInfoResponse.md)

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

