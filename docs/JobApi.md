# airflow_client.client.JobApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_jobs**](JobApi.md#get_jobs) | **GET** /api/v2/jobs | Get Jobs


# **get_jobs**
> JobCollectionResponse get_jobs(is_alive=is_alive, start_date_gte=start_date_gte, start_date_lte=start_date_lte, end_date_gte=end_date_gte, end_date_lte=end_date_lte, limit=limit, offset=offset, order_by=order_by, job_state=job_state, job_type=job_type, hostname=hostname, executor_class=executor_class)

Get Jobs

Get all jobs.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.job_collection_response import JobCollectionResponse
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
    api_instance = airflow_client.client.JobApi(api_client)
    is_alive = True # bool |  (optional)
    start_date_gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    start_date_lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date_gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date_lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)
    order_by = 'id' # str |  (optional) (default to 'id')
    job_state = 'job_state_example' # str |  (optional)
    job_type = 'job_type_example' # str |  (optional)
    hostname = 'hostname_example' # str |  (optional)
    executor_class = 'executor_class_example' # str |  (optional)

    try:
        # Get Jobs
        api_response = api_instance.get_jobs(is_alive=is_alive, start_date_gte=start_date_gte, start_date_lte=start_date_lte, end_date_gte=end_date_gte, end_date_lte=end_date_lte, limit=limit, offset=offset, order_by=order_by, job_state=job_state, job_type=job_type, hostname=hostname, executor_class=executor_class)
        print("The response of JobApi->get_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->get_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_alive** | **bool**|  | [optional] 
 **start_date_gte** | **datetime**|  | [optional] 
 **start_date_lte** | **datetime**|  | [optional] 
 **end_date_gte** | **datetime**|  | [optional] 
 **end_date_lte** | **datetime**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **order_by** | **str**|  | [optional] [default to &#39;id&#39;]
 **job_state** | **str**|  | [optional] 
 **job_type** | **str**|  | [optional] 
 **hostname** | **str**|  | [optional] 
 **executor_class** | **str**|  | [optional] 

### Return type

[**JobCollectionResponse**](JobCollectionResponse.md)

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

