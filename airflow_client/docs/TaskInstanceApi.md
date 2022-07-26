# Apache Airflow Python Client.TaskInstanceApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_extra_links**](TaskInstanceApi.md#get_extra_links) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/links | List extra links
[**get_log**](TaskInstanceApi.md#get_log) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/logs/{task_try_number} | Get logs
[**get_mapped_task_instance**](TaskInstanceApi.md#get_mapped_task_instance) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/{map_index} | Get a mapped task instance
[**get_mapped_task_instances**](TaskInstanceApi.md#get_mapped_task_instances) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/listMapped | List mapped task instances
[**get_task_instance**](TaskInstanceApi.md#get_task_instance) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id} | Get a task instance
[**get_task_instances**](TaskInstanceApi.md#get_task_instances) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances | List task instances
[**get_task_instances_batch**](TaskInstanceApi.md#get_task_instances_batch) | **POST** /dags/~/dagRuns/~/taskInstances/list | List task instances (batch)


# **get_extra_links**
> ExtraLinkCollection get_extra_links(dag_id, dag_run_id, task_id)

List extra links

List extra links for task instance. 

### Example

* Basic Authentication (Basic):

```python
import time
import airflow_client.client
from airflow_client.client.api import task_instance_api
from airflow_client.client.model.extra_link_collection import ExtraLinkCollection
from airflow_client.client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = task_instance_api.TaskInstanceApi(api_client)
    dag_id = "dag_id_example" # str | The DAG ID.
    dag_run_id = "dag_run_id_example" # str | The DAG run ID.
    task_id = "task_id_example" # str | The task ID.

    # example passing only required values which don't have defaults set
    try:
        # List extra links
        api_response = api_instance.get_extra_links(dag_id, dag_run_id, task_id)
        pprint(api_response)
    except client.ApiException as e:
        print("Exception when calling TaskInstanceApi->get_extra_links: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. |
 **dag_run_id** | **str**| The DAG run ID. |
 **task_id** | **str**| The task ID. |

### Return type

[**ExtraLinkCollection**](ExtraLinkCollection.md)

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

# **get_log**
> InlineResponse200 get_log(dag_id, dag_run_id, task_id, task_try_number)

Get logs

Get logs for a specific task instance and its try number.

### Example

* Basic Authentication (Basic):

```python
import time
import airflow_client.client
from airflow_client.client.api import task_instance_api
from airflow_client.client.model.error import Error
from airflow_client.client.model.inline_response200 import InlineResponse200
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = task_instance_api.TaskInstanceApi(api_client)
    dag_id = "dag_id_example" # str | The DAG ID.
    dag_run_id = "dag_run_id_example" # str | The DAG run ID.
    task_id = "task_id_example" # str | The task ID.
    task_try_number = 1 # int | The task try number.
    full_content = True # bool | A full content will be returned. By default, only the first fragment will be returned.  (optional)
    token = "token_example" # str | A token that allows you to continue fetching logs. If passed, it will specify the location from which the download should be continued.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get logs
        api_response = api_instance.get_log(dag_id, dag_run_id, task_id, task_try_number)
        pprint(api_response)
    except client.ApiException as e:
        print("Exception when calling TaskInstanceApi->get_log: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get logs
        api_response = api_instance.get_log(dag_id, dag_run_id, task_id, task_try_number, full_content=full_content, token=token)
        pprint(api_response)
    except client.ApiException as e:
        print("Exception when calling TaskInstanceApi->get_log: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. |
 **dag_run_id** | **str**| The DAG run ID. |
 **task_id** | **str**| The task ID. |
 **task_try_number** | **int**| The task try number. |
 **full_content** | **bool**| A full content will be returned. By default, only the first fragment will be returned.  | [optional]
 **token** | **str**| A token that allows you to continue fetching logs. If passed, it will specify the location from which the download should be continued.  | [optional]

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[Basic](../README.md#Basic), [Kerberos](../README.md#Kerberos)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Client specified an invalid argument. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |
**404** | A specified resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mapped_task_instance**
> TaskInstance get_mapped_task_instance(dag_id, dag_run_id, task_id, map_index)

Get a mapped task instance

Get details of a mapped task instance.  *New in version 2.3.0* 

### Example

* Basic Authentication (Basic):

```python
import time
import airflow_client.client
from airflow_client.client.api import task_instance_api
from airflow_client.client.model.task_instance import TaskInstance
from airflow_client.client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = task_instance_api.TaskInstanceApi(api_client)
    dag_id = "dag_id_example" # str | The DAG ID.
    dag_run_id = "dag_run_id_example" # str | The DAG run ID.
    task_id = "task_id_example" # str | The task ID.
    map_index = 1 # int | The map index.

    # example passing only required values which don't have defaults set
    try:
        # Get a mapped task instance
        api_response = api_instance.get_mapped_task_instance(dag_id, dag_run_id, task_id, map_index)
        pprint(api_response)
    except client.ApiException as e:
        print("Exception when calling TaskInstanceApi->get_mapped_task_instance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. |
 **dag_run_id** | **str**| The DAG run ID. |
 **task_id** | **str**| The task ID. |
 **map_index** | **int**| The map index. |

### Return type

[**TaskInstance**](TaskInstance.md)

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

# **get_mapped_task_instances**
> TaskInstance get_mapped_task_instances(dag_id, dag_run_id, task_id)

List mapped task instances

Get details of all mapped task instances.  *New in version 2.3.0* 

### Example

* Basic Authentication (Basic):

```python
import time
import airflow_client.client
from airflow_client.client.api import task_instance_api
from airflow_client.client.model.task_instance import TaskInstance
from airflow_client.client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = task_instance_api.TaskInstanceApi(api_client)
    dag_id = "dag_id_example" # str | The DAG ID.
    dag_run_id = "dag_run_id_example" # str | The DAG run ID.
    task_id = "task_id_example" # str | The task ID.
    limit = 100 # int | The numbers of items to return. (optional) if omitted the server will use the default value of 100
    offset = 0 # int | The number of items to skip before starting to collect the result set. (optional)
    execution_date_gte = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Returns objects greater or equal to the specified date.  This can be combined with execution_date_lte parameter to receive only the selected period.  (optional)
    execution_date_lte = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Returns objects less than or equal to the specified date.  This can be combined with execution_date_gte parameter to receive only the selected period.  (optional)
    start_date_gte = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period.  (optional)
    start_date_lte = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Returns objects less or equal the specified date.  This can be combined with start_date_gte parameter to receive only the selected period.  (optional)
    end_date_gte = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period.  (optional)
    end_date_lte = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Returns objects less than or equal to the specified date.  This can be combined with start_date_gte parameter to receive only the selected period.  (optional)
    duration_gte = 3.14 # float | Returns objects greater than or equal to the specified values.  This can be combined with duration_lte parameter to receive only the selected period.  (optional)
    duration_lte = 3.14 # float | Returns objects less than or equal to the specified values.  This can be combined with duration_gte parameter to receive only the selected range.  (optional)
    state = [
        "state_example",
    ] # [str] | The value can be repeated to retrieve multiple matching values (OR condition). (optional)
    pool = [
        "pool_example",
    ] # [str] | The value can be repeated to retrieve multiple matching values (OR condition). (optional)
    queue = [
        "queue_example",
    ] # [str] | The value can be repeated to retrieve multiple matching values (OR condition). (optional)
    order_by = "order_by_example" # str | The name of the field to order the results by. Prefix a field name with `-` to reverse the sort order.  *New in version 2.1.0*  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List mapped task instances
        api_response = api_instance.get_mapped_task_instances(dag_id, dag_run_id, task_id)
        pprint(api_response)
    except client.ApiException as e:
        print("Exception when calling TaskInstanceApi->get_mapped_task_instances: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List mapped task instances
        api_response = api_instance.get_mapped_task_instances(dag_id, dag_run_id, task_id, limit=limit, offset=offset, execution_date_gte=execution_date_gte, execution_date_lte=execution_date_lte, start_date_gte=start_date_gte, start_date_lte=start_date_lte, end_date_gte=end_date_gte, end_date_lte=end_date_lte, duration_gte=duration_gte, duration_lte=duration_lte, state=state, pool=pool, queue=queue, order_by=order_by)
        pprint(api_response)
    except client.ApiException as e:
        print("Exception when calling TaskInstanceApi->get_mapped_task_instances: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. |
 **dag_run_id** | **str**| The DAG run ID. |
 **task_id** | **str**| The task ID. |
 **limit** | **int**| The numbers of items to return. | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional]
 **execution_date_gte** | **datetime**| Returns objects greater or equal to the specified date.  This can be combined with execution_date_lte parameter to receive only the selected period.  | [optional]
 **execution_date_lte** | **datetime**| Returns objects less than or equal to the specified date.  This can be combined with execution_date_gte parameter to receive only the selected period.  | [optional]
 **start_date_gte** | **datetime**| Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period.  | [optional]
 **start_date_lte** | **datetime**| Returns objects less or equal the specified date.  This can be combined with start_date_gte parameter to receive only the selected period.  | [optional]
 **end_date_gte** | **datetime**| Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period.  | [optional]
 **end_date_lte** | **datetime**| Returns objects less than or equal to the specified date.  This can be combined with start_date_gte parameter to receive only the selected period.  | [optional]
 **duration_gte** | **float**| Returns objects greater than or equal to the specified values.  This can be combined with duration_lte parameter to receive only the selected period.  | [optional]
 **duration_lte** | **float**| Returns objects less than or equal to the specified values.  This can be combined with duration_gte parameter to receive only the selected range.  | [optional]
 **state** | **[str]**| The value can be repeated to retrieve multiple matching values (OR condition). | [optional]
 **pool** | **[str]**| The value can be repeated to retrieve multiple matching values (OR condition). | [optional]
 **queue** | **[str]**| The value can be repeated to retrieve multiple matching values (OR condition). | [optional]
 **order_by** | **str**| The name of the field to order the results by. Prefix a field name with &#x60;-&#x60; to reverse the sort order.  *New in version 2.1.0*  | [optional]

### Return type

[**TaskInstance**](TaskInstance.md)

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

# **get_task_instance**
> TaskInstance get_task_instance(dag_id, dag_run_id, task_id)

Get a task instance

### Example

* Basic Authentication (Basic):

```python
import time
import airflow_client.client
from airflow_client.client.api import task_instance_api
from airflow_client.client.model.task_instance import TaskInstance
from airflow_client.client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = task_instance_api.TaskInstanceApi(api_client)
    dag_id = "dag_id_example" # str | The DAG ID.
    dag_run_id = "dag_run_id_example" # str | The DAG run ID.
    task_id = "task_id_example" # str | The task ID.

    # example passing only required values which don't have defaults set
    try:
        # Get a task instance
        api_response = api_instance.get_task_instance(dag_id, dag_run_id, task_id)
        pprint(api_response)
    except client.ApiException as e:
        print("Exception when calling TaskInstanceApi->get_task_instance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. |
 **dag_run_id** | **str**| The DAG run ID. |
 **task_id** | **str**| The task ID. |

### Return type

[**TaskInstance**](TaskInstance.md)

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

# **get_task_instances**
> TaskInstanceCollection get_task_instances(dag_id, dag_run_id)

List task instances

This endpoint allows specifying `~` as the dag_id, dag_run_id to retrieve DAG runs for all DAGs and DAG runs. 

### Example

* Basic Authentication (Basic):

```python
import time
import airflow_client.client
from airflow_client.client.api import task_instance_api
from airflow_client.client.model.task_instance_collection import TaskInstanceCollection
from airflow_client.client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = task_instance_api.TaskInstanceApi(api_client)
    dag_id = "dag_id_example" # str | The DAG ID.
    dag_run_id = "dag_run_id_example" # str | The DAG run ID.
    execution_date_gte = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Returns objects greater or equal to the specified date.  This can be combined with execution_date_lte parameter to receive only the selected period.  (optional)
    execution_date_lte = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Returns objects less than or equal to the specified date.  This can be combined with execution_date_gte parameter to receive only the selected period.  (optional)
    start_date_gte = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period.  (optional)
    start_date_lte = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Returns objects less or equal the specified date.  This can be combined with start_date_gte parameter to receive only the selected period.  (optional)
    end_date_gte = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period.  (optional)
    end_date_lte = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Returns objects less than or equal to the specified date.  This can be combined with start_date_gte parameter to receive only the selected period.  (optional)
    duration_gte = 3.14 # float | Returns objects greater than or equal to the specified values.  This can be combined with duration_lte parameter to receive only the selected period.  (optional)
    duration_lte = 3.14 # float | Returns objects less than or equal to the specified values.  This can be combined with duration_gte parameter to receive only the selected range.  (optional)
    state = [
        "state_example",
    ] # [str] | The value can be repeated to retrieve multiple matching values (OR condition). (optional)
    pool = [
        "pool_example",
    ] # [str] | The value can be repeated to retrieve multiple matching values (OR condition). (optional)
    queue = [
        "queue_example",
    ] # [str] | The value can be repeated to retrieve multiple matching values (OR condition). (optional)
    limit = 100 # int | The numbers of items to return. (optional) if omitted the server will use the default value of 100
    offset = 0 # int | The number of items to skip before starting to collect the result set. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List task instances
        api_response = api_instance.get_task_instances(dag_id, dag_run_id)
        pprint(api_response)
    except client.ApiException as e:
        print("Exception when calling TaskInstanceApi->get_task_instances: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List task instances
        api_response = api_instance.get_task_instances(dag_id, dag_run_id, execution_date_gte=execution_date_gte, execution_date_lte=execution_date_lte, start_date_gte=start_date_gte, start_date_lte=start_date_lte, end_date_gte=end_date_gte, end_date_lte=end_date_lte, duration_gte=duration_gte, duration_lte=duration_lte, state=state, pool=pool, queue=queue, limit=limit, offset=offset)
        pprint(api_response)
    except client.ApiException as e:
        print("Exception when calling TaskInstanceApi->get_task_instances: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. |
 **dag_run_id** | **str**| The DAG run ID. |
 **execution_date_gte** | **datetime**| Returns objects greater or equal to the specified date.  This can be combined with execution_date_lte parameter to receive only the selected period.  | [optional]
 **execution_date_lte** | **datetime**| Returns objects less than or equal to the specified date.  This can be combined with execution_date_gte parameter to receive only the selected period.  | [optional]
 **start_date_gte** | **datetime**| Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period.  | [optional]
 **start_date_lte** | **datetime**| Returns objects less or equal the specified date.  This can be combined with start_date_gte parameter to receive only the selected period.  | [optional]
 **end_date_gte** | **datetime**| Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period.  | [optional]
 **end_date_lte** | **datetime**| Returns objects less than or equal to the specified date.  This can be combined with start_date_gte parameter to receive only the selected period.  | [optional]
 **duration_gte** | **float**| Returns objects greater than or equal to the specified values.  This can be combined with duration_lte parameter to receive only the selected period.  | [optional]
 **duration_lte** | **float**| Returns objects less than or equal to the specified values.  This can be combined with duration_gte parameter to receive only the selected range.  | [optional]
 **state** | **[str]**| The value can be repeated to retrieve multiple matching values (OR condition). | [optional]
 **pool** | **[str]**| The value can be repeated to retrieve multiple matching values (OR condition). | [optional]
 **queue** | **[str]**| The value can be repeated to retrieve multiple matching values (OR condition). | [optional]
 **limit** | **int**| The numbers of items to return. | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional]

### Return type

[**TaskInstanceCollection**](TaskInstanceCollection.md)

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

# **get_task_instances_batch**
> TaskInstanceCollection get_task_instances_batch(list_task_instance_form)

List task instances (batch)

List task instances from all DAGs and DAG runs. This endpoint is a POST to allow filtering across a large number of DAG IDs, where as a GET it would run in to maximum HTTP request URL length limits. 

### Example

* Basic Authentication (Basic):

```python
import time
import airflow_client.client
from airflow_client.client.api import task_instance_api
from airflow_client.client.model.task_instance_collection import TaskInstanceCollection
from airflow_client.client.model.error import Error
from airflow_client.client.model.list_task_instance_form import ListTaskInstanceForm
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = task_instance_api.TaskInstanceApi(api_client)
    list_task_instance_form = ListTaskInstanceForm(
        dag_ids=[
            "dag_ids_example",
        ],
        execution_date_gte=dateutil_parser('1970-01-01T00:00:00.00Z'),
        execution_date_lte=dateutil_parser('1970-01-01T00:00:00.00Z'),
        start_date_gte=dateutil_parser('1970-01-01T00:00:00.00Z'),
        start_date_lte=dateutil_parser('1970-01-01T00:00:00.00Z'),
        end_date_gte=dateutil_parser('1970-01-01T00:00:00.00Z'),
        end_date_lte=dateutil_parser('1970-01-01T00:00:00.00Z'),
        duration_gte=3.14,
        duration_lte=3.14,
        state=[
            TaskState("success"),
        ],
        pool=[
            "pool_example",
        ],
        queue=[
            "queue_example",
        ],
    ) # ListTaskInstanceForm | 

    # example passing only required values which don't have defaults set
    try:
        # List task instances (batch)
        api_response = api_instance.get_task_instances_batch(list_task_instance_form)
        pprint(api_response)
    except client.ApiException as e:
        print("Exception when calling TaskInstanceApi->get_task_instances_batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_task_instance_form** | [**ListTaskInstanceForm**](ListTaskInstanceForm.md)|  |

### Return type

[**TaskInstanceCollection**](TaskInstanceCollection.md)

### Authorization

[Basic](../README.md#Basic), [Kerberos](../README.md#Kerberos)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |
**404** | A specified resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

