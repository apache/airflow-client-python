# airflow_client.client.EventLogApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_event_log**](EventLogApi.md#get_event_log) | **GET** /api/v2/eventLogs/{event_log_id} | Get Event Log
[**get_event_logs**](EventLogApi.md#get_event_logs) | **GET** /api/v2/eventLogs | Get Event Logs


# **get_event_log**
> EventLogResponse get_event_log(event_log_id)

Get Event Log

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

```python
import airflow_client.client
from airflow_client.client.models.event_log_response import EventLogResponse
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
    api_instance = airflow_client.client.EventLogApi(api_client)
    event_log_id = 56 # int | 

    try:
        # Get Event Log
        api_response = api_instance.get_event_log(event_log_id)
        print("The response of EventLogApi->get_event_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventLogApi->get_event_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_log_id** | **int**|  | 

### Return type

[**EventLogResponse**](EventLogResponse.md)

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

# **get_event_logs**
> EventLogCollectionResponse get_event_logs(limit=limit, offset=offset, order_by=order_by, dag_id=dag_id, task_id=task_id, run_id=run_id, map_index=map_index, try_number=try_number, owner=owner, event=event, excluded_events=excluded_events, included_events=included_events, before=before, after=after, dag_id_pattern=dag_id_pattern, task_id_pattern=task_id_pattern, run_id_pattern=run_id_pattern, owner_pattern=owner_pattern, event_pattern=event_pattern)

Get Event Logs

Get all Event Logs.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

```python
import airflow_client.client
from airflow_client.client.models.event_log_collection_response import EventLogCollectionResponse
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
    api_instance = airflow_client.client.EventLogApi(api_client)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)
    order_by = [id] # List[str] |  (optional) (default to [id])
    dag_id = 'dag_id_example' # str |  (optional)
    task_id = 'task_id_example' # str |  (optional)
    run_id = 'run_id_example' # str |  (optional)
    map_index = 56 # int |  (optional)
    try_number = 56 # int |  (optional)
    owner = 'owner_example' # str |  (optional)
    event = 'event_example' # str |  (optional)
    excluded_events = ['excluded_events_example'] # List[str] |  (optional)
    included_events = ['included_events_example'] # List[str] |  (optional)
    before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    dag_id_pattern = 'dag_id_pattern_example' # str | SQL LIKE expression — use `%` / `_` wildcards (e.g. `%customer_%`). Regular expressions are **not** supported. (optional)
    task_id_pattern = 'task_id_pattern_example' # str | SQL LIKE expression — use `%` / `_` wildcards (e.g. `%customer_%`). Regular expressions are **not** supported. (optional)
    run_id_pattern = 'run_id_pattern_example' # str | SQL LIKE expression — use `%` / `_` wildcards (e.g. `%customer_%`). Regular expressions are **not** supported. (optional)
    owner_pattern = 'owner_pattern_example' # str | SQL LIKE expression — use `%` / `_` wildcards (e.g. `%customer_%`). Regular expressions are **not** supported. (optional)
    event_pattern = 'event_pattern_example' # str | SQL LIKE expression — use `%` / `_` wildcards (e.g. `%customer_%`). Regular expressions are **not** supported. (optional)

    try:
        # Get Event Logs
        api_response = api_instance.get_event_logs(limit=limit, offset=offset, order_by=order_by, dag_id=dag_id, task_id=task_id, run_id=run_id, map_index=map_index, try_number=try_number, owner=owner, event=event, excluded_events=excluded_events, included_events=included_events, before=before, after=after, dag_id_pattern=dag_id_pattern, task_id_pattern=task_id_pattern, run_id_pattern=run_id_pattern, owner_pattern=owner_pattern, event_pattern=event_pattern)
        print("The response of EventLogApi->get_event_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventLogApi->get_event_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **order_by** | [**List[str]**](str.md)|  | [optional] [default to [id]]
 **dag_id** | **str**|  | [optional] 
 **task_id** | **str**|  | [optional] 
 **run_id** | **str**|  | [optional] 
 **map_index** | **int**|  | [optional] 
 **try_number** | **int**|  | [optional] 
 **owner** | **str**|  | [optional] 
 **event** | **str**|  | [optional] 
 **excluded_events** | [**List[str]**](str.md)|  | [optional] 
 **included_events** | [**List[str]**](str.md)|  | [optional] 
 **before** | **datetime**|  | [optional] 
 **after** | **datetime**|  | [optional] 
 **dag_id_pattern** | **str**| SQL LIKE expression — use &#x60;%&#x60; / &#x60;_&#x60; wildcards (e.g. &#x60;%customer_%&#x60;). Regular expressions are **not** supported. | [optional] 
 **task_id_pattern** | **str**| SQL LIKE expression — use &#x60;%&#x60; / &#x60;_&#x60; wildcards (e.g. &#x60;%customer_%&#x60;). Regular expressions are **not** supported. | [optional] 
 **run_id_pattern** | **str**| SQL LIKE expression — use &#x60;%&#x60; / &#x60;_&#x60; wildcards (e.g. &#x60;%customer_%&#x60;). Regular expressions are **not** supported. | [optional] 
 **owner_pattern** | **str**| SQL LIKE expression — use &#x60;%&#x60; / &#x60;_&#x60; wildcards (e.g. &#x60;%customer_%&#x60;). Regular expressions are **not** supported. | [optional] 
 **event_pattern** | **str**| SQL LIKE expression — use &#x60;%&#x60; / &#x60;_&#x60; wildcards (e.g. &#x60;%customer_%&#x60;). Regular expressions are **not** supported. | [optional] 

### Return type

[**EventLogCollectionResponse**](EventLogCollectionResponse.md)

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

