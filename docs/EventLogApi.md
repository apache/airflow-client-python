# airflow_client.client.EventLogApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_event_log**](EventLogApi.md#get_event_log) | **GET** /eventLogs/{event_log_id} | Get a log entry
[**get_event_logs**](EventLogApi.md#get_event_logs) | **GET** /eventLogs | List log entries


# **get_event_log**
> EventLog get_event_log(event_log_id)

Get a log entry

### Example

* Basic Authentication (Basic):

```python
import time
import airflow_client.client
from airflow_client.client.api import event_log_api
from airflow_client.client.model.event_log import EventLog
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
    api_instance = event_log_api.EventLogApi(api_client)
    event_log_id = 1 # int | The event log ID.

    # example passing only required values which don't have defaults set
    try:
        # Get a log entry
        api_response = api_instance.get_event_log(event_log_id)
        pprint(api_response)
    except airflow_client.client.ApiException as e:
        print("Exception when calling EventLogApi->get_event_log: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_log_id** | **int**| The event log ID. |

### Return type

[**EventLog**](EventLog.md)

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
**404** | A specified resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_logs**
> EventLogCollection get_event_logs()

List log entries

List log entries from event log.

### Example

* Basic Authentication (Basic):

```python
import time
import airflow_client.client
from airflow_client.client.api import event_log_api
from airflow_client.client.model.event_log_collection import EventLogCollection
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
    api_instance = event_log_api.EventLogApi(api_client)
    limit = 100 # int | The numbers of items to return. (optional) if omitted the server will use the default value of 100
    offset = 0 # int | The number of items to skip before starting to collect the result set. (optional)
    order_by = "order_by_example" # str | The name of the field to order the results by. Prefix a field name with `-` to reverse the sort order.  *New in version 2.1.0*  (optional)
    dag_id = "dag_id_example" # str | Returns objects matched by the DAG ID. (optional)
    task_id = "task_id_example" # str | Returns objects matched by the Task ID. (optional)
    run_id = "run_id_example" # str | Returns objects matched by the Run ID. (optional)
    map_index = 1 # int | Filter on map index for mapped task. (optional)
    try_number = 1 # int | Filter on try_number for task instance. (optional)
    event = "event_example" # str | The name of event log. (optional)
    owner = "owner_example" # str | The owner's name of event log. (optional)
    before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Timestamp to select event logs occurring before. (optional)
    after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Timestamp to select event logs occurring after. (optional)
    included_events = "included_events_example" # str | One or more event names separated by commas. If set, only return event logs with events matching this pattern. *New in version 2.9.0*  (optional)
    excluded_events = "excluded_events_example" # str | One or more event names separated by commas. If set, only return event logs with events that do not match this pattern. *New in version 2.9.0*  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List log entries
        api_response = api_instance.get_event_logs(limit=limit, offset=offset, order_by=order_by, dag_id=dag_id, task_id=task_id, run_id=run_id, map_index=map_index, try_number=try_number, event=event, owner=owner, before=before, after=after, included_events=included_events, excluded_events=excluded_events)
        pprint(api_response)
    except airflow_client.client.ApiException as e:
        print("Exception when calling EventLogApi->get_event_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The numbers of items to return. | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional]
 **order_by** | **str**| The name of the field to order the results by. Prefix a field name with &#x60;-&#x60; to reverse the sort order.  *New in version 2.1.0*  | [optional]
 **dag_id** | **str**| Returns objects matched by the DAG ID. | [optional]
 **task_id** | **str**| Returns objects matched by the Task ID. | [optional]
 **run_id** | **str**| Returns objects matched by the Run ID. | [optional]
 **map_index** | **int**| Filter on map index for mapped task. | [optional]
 **try_number** | **int**| Filter on try_number for task instance. | [optional]
 **event** | **str**| The name of event log. | [optional]
 **owner** | **str**| The owner&#39;s name of event log. | [optional]
 **before** | **datetime**| Timestamp to select event logs occurring before. | [optional]
 **after** | **datetime**| Timestamp to select event logs occurring after. | [optional]
 **included_events** | **str**| One or more event names separated by commas. If set, only return event logs with events matching this pattern. *New in version 2.9.0*  | [optional]
 **excluded_events** | **str**| One or more event names separated by commas. If set, only return event logs with events that do not match this pattern. *New in version 2.9.0*  | [optional]

### Return type

[**EventLogCollection**](EventLogCollection.md)

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

