<!--
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements.  See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership.  The ASF licenses this file
 to you under the Apache License, Version 2.0 (the
 "License"); you may not use this file except in compliance
 with the License.  You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing,
 software distributed under the License is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied.  See the License for the
 specific language governing permissions and limitations
 under the License.
 -->

# Apache Airflow Python Client.DAGRunApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_dag_run**](DAGRunApi.md#clear_dag_run) | **POST** /dags/{dag_id}/dagRuns/{dag_run_id}/clear | Clear a DAG run
[**delete_dag_run**](DAGRunApi.md#delete_dag_run) | **DELETE** /dags/{dag_id}/dagRuns/{dag_run_id} | Delete a DAG run
[**get_dag_run**](DAGRunApi.md#get_dag_run) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id} | Get a DAG run
[**get_dag_runs**](DAGRunApi.md#get_dag_runs) | **GET** /dags/{dag_id}/dagRuns | List DAG runs
[**get_dag_runs_batch**](DAGRunApi.md#get_dag_runs_batch) | **POST** /dags/~/dagRuns/list | List DAG runs (batch)
[**get_upstream_dataset_events**](DAGRunApi.md#get_upstream_dataset_events) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/upstreamDatasetEvents | Get dataset events for a DAG run
[**post_dag_run**](DAGRunApi.md#post_dag_run) | **POST** /dags/{dag_id}/dagRuns | Trigger a new DAG run
[**update_dag_run_state**](DAGRunApi.md#update_dag_run_state) | **PATCH** /dags/{dag_id}/dagRuns/{dag_run_id} | Modify a DAG run


# **clear_dag_run**
> DAGRun clear_dag_run(dag_id, dag_run_id, clear_dag_run)

Clear a DAG run

Clear a DAG run.  *New in version 2.4.0* 

### Example

* Basic Authentication (Basic):

```python
import time
import airflow_client.client
from airflow_client.client.api import dag_run_api
from airflow_client.client.model.clear_dag_run import ClearDagRun
from airflow_client.client.model.dag_run import DAGRun
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
    api_instance = dag_run_api.DAGRunApi(api_client)
    dag_id = "dag_id_example" # str | The DAG ID.
    dag_run_id = "dag_run_id_example" # str | The DAG run ID.
    clear_dag_run = ClearDagRun(
        dry_run=True,
    ) # ClearDagRun | 

    # example passing only required values which don't have defaults set
    try:
        # Clear a DAG run
        api_response = api_instance.clear_dag_run(dag_id, dag_run_id, clear_dag_run)
        pprint(api_response)
    except client.ApiException as e:
        print("Exception when calling DAGRunApi->clear_dag_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. |
 **dag_run_id** | **str**| The DAG run ID. |
 **clear_dag_run** | [**ClearDagRun**](ClearDagRun.md)|  |

### Return type

[**DAGRun**](DAGRun.md)

### Authorization

[Basic](../README.md#Basic), [Kerberos](../README.md#Kerberos)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Client specified an invalid argument. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |
**404** | A specified resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dag_run**
> delete_dag_run(dag_id, dag_run_id)

Delete a DAG run

### Example

* Basic Authentication (Basic):

```python
import time
import airflow_client.client
from airflow_client.client.api import dag_run_api
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
    api_instance = dag_run_api.DAGRunApi(api_client)
    dag_id = "dag_id_example" # str | The DAG ID.
    dag_run_id = "dag_run_id_example" # str | The DAG run ID.

    # example passing only required values which don't have defaults set
    try:
        # Delete a DAG run
        api_instance.delete_dag_run(dag_id, dag_run_id)
    except client.ApiException as e:
        print("Exception when calling DAGRunApi->delete_dag_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. |
 **dag_run_id** | **str**| The DAG run ID. |

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [Kerberos](../README.md#Kerberos)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success. |  -  |
**400** | Client specified an invalid argument. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |
**404** | A specified resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dag_run**
> DAGRun get_dag_run(dag_id, dag_run_id)

Get a DAG run

### Example

* Basic Authentication (Basic):

```python
import time
import airflow_client.client
from airflow_client.client.api import dag_run_api
from airflow_client.client.model.dag_run import DAGRun
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
    api_instance = dag_run_api.DAGRunApi(api_client)
    dag_id = "dag_id_example" # str | The DAG ID.
    dag_run_id = "dag_run_id_example" # str | The DAG run ID.

    # example passing only required values which don't have defaults set
    try:
        # Get a DAG run
        api_response = api_instance.get_dag_run(dag_id, dag_run_id)
        pprint(api_response)
    except client.ApiException as e:
        print("Exception when calling DAGRunApi->get_dag_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. |
 **dag_run_id** | **str**| The DAG run ID. |

### Return type

[**DAGRun**](DAGRun.md)

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

# **get_dag_runs**
> DAGRunCollection get_dag_runs(dag_id)

List DAG runs

This endpoint allows specifying `~` as the dag_id to retrieve DAG runs for all DAGs. 

### Example

* Basic Authentication (Basic):

```python
import time
import airflow_client.client
from airflow_client.client.api import dag_run_api
from airflow_client.client.model.dag_run_collection import DAGRunCollection
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
    api_instance = dag_run_api.DAGRunApi(api_client)
    dag_id = "dag_id_example" # str | The DAG ID.
    limit = 100 # int | The numbers of items to return. (optional) if omitted the server will use the default value of 100
    offset = 0 # int | The number of items to skip before starting to collect the result set. (optional)
    execution_date_gte = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Returns objects greater or equal to the specified date.  This can be combined with execution_date_lte parameter to receive only the selected period.  (optional)
    execution_date_lte = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Returns objects less than or equal to the specified date.  This can be combined with execution_date_gte parameter to receive only the selected period.  (optional)
    start_date_gte = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period.  (optional)
    start_date_lte = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Returns objects less or equal the specified date.  This can be combined with start_date_gte parameter to receive only the selected period.  (optional)
    end_date_gte = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period.  (optional)
    end_date_lte = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Returns objects less than or equal to the specified date.  This can be combined with start_date_gte parameter to receive only the selected period.  (optional)
    state = [
        "state_example",
    ] # [str] | The value can be repeated to retrieve multiple matching values (OR condition). (optional)
    order_by = "order_by_example" # str | The name of the field to order the results by. Prefix a field name with `-` to reverse the sort order.  *New in version 2.1.0*  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List DAG runs
        api_response = api_instance.get_dag_runs(dag_id)
        pprint(api_response)
    except client.ApiException as e:
        print("Exception when calling DAGRunApi->get_dag_runs: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List DAG runs
        api_response = api_instance.get_dag_runs(dag_id, limit=limit, offset=offset, execution_date_gte=execution_date_gte, execution_date_lte=execution_date_lte, start_date_gte=start_date_gte, start_date_lte=start_date_lte, end_date_gte=end_date_gte, end_date_lte=end_date_lte, state=state, order_by=order_by)
        pprint(api_response)
    except client.ApiException as e:
        print("Exception when calling DAGRunApi->get_dag_runs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. |
 **limit** | **int**| The numbers of items to return. | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional]
 **execution_date_gte** | **datetime**| Returns objects greater or equal to the specified date.  This can be combined with execution_date_lte parameter to receive only the selected period.  | [optional]
 **execution_date_lte** | **datetime**| Returns objects less than or equal to the specified date.  This can be combined with execution_date_gte parameter to receive only the selected period.  | [optional]
 **start_date_gte** | **datetime**| Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period.  | [optional]
 **start_date_lte** | **datetime**| Returns objects less or equal the specified date.  This can be combined with start_date_gte parameter to receive only the selected period.  | [optional]
 **end_date_gte** | **datetime**| Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period.  | [optional]
 **end_date_lte** | **datetime**| Returns objects less than or equal to the specified date.  This can be combined with start_date_gte parameter to receive only the selected period.  | [optional]
 **state** | **[str]**| The value can be repeated to retrieve multiple matching values (OR condition). | [optional]
 **order_by** | **str**| The name of the field to order the results by. Prefix a field name with &#x60;-&#x60; to reverse the sort order.  *New in version 2.1.0*  | [optional]

### Return type

[**DAGRunCollection**](DAGRunCollection.md)

### Authorization

[Basic](../README.md#Basic), [Kerberos](../README.md#Kerberos)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of DAG runs. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dag_runs_batch**
> DAGRunCollection get_dag_runs_batch(list_dag_runs_form)

List DAG runs (batch)

This endpoint is a POST to allow filtering across a large number of DAG IDs, where as a GET it would run in to maximum HTTP request URL length limit. 

### Example

* Basic Authentication (Basic):

```python
import time
import airflow_client.client
from airflow_client.client.api import dag_run_api
from airflow_client.client.model.list_dag_runs_form import ListDagRunsForm
from airflow_client.client.model.dag_run_collection import DAGRunCollection
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
    api_instance = dag_run_api.DAGRunApi(api_client)
    list_dag_runs_form = ListDagRunsForm(
        order_by="order_by_example",
        page_offset=0,
        page_limit=100,
        dag_ids=[
            "dag_ids_example",
        ],
        states=[
            "states_example",
        ],
        execution_date_gte=dateutil_parser('1970-01-01T00:00:00.00Z'),
        execution_date_lte=dateutil_parser('1970-01-01T00:00:00.00Z'),
        start_date_gte=dateutil_parser('1970-01-01T00:00:00.00Z'),
        start_date_lte=dateutil_parser('1970-01-01T00:00:00.00Z'),
        end_date_gte=dateutil_parser('1970-01-01T00:00:00.00Z'),
        end_date_lte=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # ListDagRunsForm | 

    # example passing only required values which don't have defaults set
    try:
        # List DAG runs (batch)
        api_response = api_instance.get_dag_runs_batch(list_dag_runs_form)
        pprint(api_response)
    except client.ApiException as e:
        print("Exception when calling DAGRunApi->get_dag_runs_batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_dag_runs_form** | [**ListDagRunsForm**](ListDagRunsForm.md)|  |

### Return type

[**DAGRunCollection**](DAGRunCollection.md)

### Authorization

[Basic](../README.md#Basic), [Kerberos](../README.md#Kerberos)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Client specified an invalid argument. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upstream_dataset_events**
> DatasetEventCollection get_upstream_dataset_events(dag_id, dag_run_id)

Get dataset events for a DAG run

Get datasets for a dag run.  *New in version 2.4.0* 

### Example

* Basic Authentication (Basic):

```python
import time
import airflow_client.client
from airflow_client.client.api import dag_run_api
from airflow_client.client.model.dataset_event_collection import DatasetEventCollection
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
    api_instance = dag_run_api.DAGRunApi(api_client)
    dag_id = "dag_id_example" # str | The DAG ID.
    dag_run_id = "dag_run_id_example" # str | The DAG run ID.

    # example passing only required values which don't have defaults set
    try:
        # Get dataset events for a DAG run
        api_response = api_instance.get_upstream_dataset_events(dag_id, dag_run_id)
        pprint(api_response)
    except client.ApiException as e:
        print("Exception when calling DAGRunApi->get_upstream_dataset_events: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. |
 **dag_run_id** | **str**| The DAG run ID. |

### Return type

[**DatasetEventCollection**](DatasetEventCollection.md)

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

# **post_dag_run**
> DAGRun post_dag_run(dag_id, dag_run)

Trigger a new DAG run

### Example

* Basic Authentication (Basic):

```python
import time
import airflow_client.client
from airflow_client.client.api import dag_run_api
from airflow_client.client.model.dag_run import DAGRun
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
    api_instance = dag_run_api.DAGRunApi(api_client)
    dag_id = "dag_id_example" # str | The DAG ID.
    dag_run = DAGRun(
        dag_run_id="dag_run_id_example",
        logical_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        execution_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        state=DagState("queued"),
        conf={},
    ) # DAGRun | 

    # example passing only required values which don't have defaults set
    try:
        # Trigger a new DAG run
        api_response = api_instance.post_dag_run(dag_id, dag_run)
        pprint(api_response)
    except client.ApiException as e:
        print("Exception when calling DAGRunApi->post_dag_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. |
 **dag_run** | [**DAGRun**](DAGRun.md)|  |

### Return type

[**DAGRun**](DAGRun.md)

### Authorization

[Basic](../README.md#Basic), [Kerberos](../README.md#Kerberos)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Client specified an invalid argument. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**409** | An existing resource conflicts with the request. |  -  |
**403** | Client does not have sufficient permission. |  -  |
**404** | A specified resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dag_run_state**
> DAGRun update_dag_run_state(dag_id, dag_run_id, update_dag_run_state)

Modify a DAG run

Modify a DAG run.  *New in version 2.2.0* 

### Example

* Basic Authentication (Basic):

```python
import time
import airflow_client.client
from airflow_client.client.api import dag_run_api
from airflow_client.client.model.dag_run import DAGRun
from airflow_client.client.model.update_dag_run_state import UpdateDagRunState
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
    api_instance = dag_run_api.DAGRunApi(api_client)
    dag_id = "dag_id_example" # str | The DAG ID.
    dag_run_id = "dag_run_id_example" # str | The DAG run ID.
    update_dag_run_state = UpdateDagRunState(
        state="success",
    ) # UpdateDagRunState | 

    # example passing only required values which don't have defaults set
    try:
        # Modify a DAG run
        api_response = api_instance.update_dag_run_state(dag_id, dag_run_id, update_dag_run_state)
        pprint(api_response)
    except client.ApiException as e:
        print("Exception when calling DAGRunApi->update_dag_run_state: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. |
 **dag_run_id** | **str**| The DAG run ID. |
 **update_dag_run_state** | [**UpdateDagRunState**](UpdateDagRunState.md)|  |

### Return type

[**DAGRun**](DAGRun.md)

### Authorization

[Basic](../README.md#Basic), [Kerberos](../README.md#Kerberos)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Client specified an invalid argument. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |
**404** | A specified resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

