# airflow_client.client.AssetApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_asset_event**](AssetApi.md#create_asset_event) | **POST** /api/v2/assets/events | Create Asset Event
[**delete_asset_queued_events**](AssetApi.md#delete_asset_queued_events) | **DELETE** /api/v2/assets/{asset_id}/queuedEvents | Delete Asset Queued Events
[**delete_dag_asset_queued_event**](AssetApi.md#delete_dag_asset_queued_event) | **DELETE** /api/v2/dags/{dag_id}/assets/{asset_id}/queuedEvents | Delete Dag Asset Queued Event
[**delete_dag_asset_queued_events**](AssetApi.md#delete_dag_asset_queued_events) | **DELETE** /api/v2/dags/{dag_id}/assets/queuedEvents | Delete Dag Asset Queued Events
[**get_asset**](AssetApi.md#get_asset) | **GET** /api/v2/assets/{asset_id} | Get Asset
[**get_asset_alias**](AssetApi.md#get_asset_alias) | **GET** /api/v2/assets/aliases/{asset_alias_id} | Get Asset Alias
[**get_asset_aliases**](AssetApi.md#get_asset_aliases) | **GET** /api/v2/assets/aliases | Get Asset Aliases
[**get_asset_events**](AssetApi.md#get_asset_events) | **GET** /api/v2/assets/events | Get Asset Events
[**get_asset_queued_events**](AssetApi.md#get_asset_queued_events) | **GET** /api/v2/assets/{asset_id}/queuedEvents | Get Asset Queued Events
[**get_assets**](AssetApi.md#get_assets) | **GET** /api/v2/assets | Get Assets
[**get_dag_asset_queued_event**](AssetApi.md#get_dag_asset_queued_event) | **GET** /api/v2/dags/{dag_id}/assets/{asset_id}/queuedEvents | Get Dag Asset Queued Event
[**get_dag_asset_queued_events**](AssetApi.md#get_dag_asset_queued_events) | **GET** /api/v2/dags/{dag_id}/assets/queuedEvents | Get Dag Asset Queued Events
[**materialize_asset**](AssetApi.md#materialize_asset) | **POST** /api/v2/assets/{asset_id}/materialize | Materialize Asset


# **create_asset_event**
> AssetEventResponse create_asset_event(create_asset_events_body)

Create Asset Event

Create asset events.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.asset_event_response import AssetEventResponse
from airflow_client.client.models.create_asset_events_body import CreateAssetEventsBody
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
    api_instance = airflow_client.client.AssetApi(api_client)
    create_asset_events_body = airflow_client.client.CreateAssetEventsBody() # CreateAssetEventsBody | 

    try:
        # Create Asset Event
        api_response = api_instance.create_asset_event(create_asset_events_body)
        print("The response of AssetApi->create_asset_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->create_asset_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_asset_events_body** | [**CreateAssetEventsBody**](CreateAssetEventsBody.md)|  | 

### Return type

[**AssetEventResponse**](AssetEventResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
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

# **delete_asset_queued_events**
> delete_asset_queued_events(asset_id, before=before)

Delete Asset Queued Events

Delete queued asset events for an asset.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
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
    api_instance = airflow_client.client.AssetApi(api_client)
    asset_id = 56 # int | 
    before = 'before_example' # str |  (optional)

    try:
        # Delete Asset Queued Events
        api_instance.delete_asset_queued_events(asset_id, before=before)
    except Exception as e:
        print("Exception when calling AssetApi->delete_asset_queued_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**|  | 
 **before** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dag_asset_queued_event**
> delete_dag_asset_queued_event(dag_id, asset_id, before=before)

Delete Dag Asset Queued Event

Delete a queued asset event for a DAG.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
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
    api_instance = airflow_client.client.AssetApi(api_client)
    dag_id = 'dag_id_example' # str | 
    asset_id = 56 # int | 
    before = 'before_example' # str |  (optional)

    try:
        # Delete Dag Asset Queued Event
        api_instance.delete_dag_asset_queued_event(dag_id, asset_id, before=before)
    except Exception as e:
        print("Exception when calling AssetApi->delete_dag_asset_queued_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **asset_id** | **int**|  | 
 **before** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dag_asset_queued_events**
> delete_dag_asset_queued_events(dag_id, before=before)

Delete Dag Asset Queued Events

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
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
    api_instance = airflow_client.client.AssetApi(api_client)
    dag_id = 'dag_id_example' # str | 
    before = 'before_example' # str |  (optional)

    try:
        # Delete Dag Asset Queued Events
        api_instance.delete_dag_asset_queued_events(dag_id, before=before)
    except Exception as e:
        print("Exception when calling AssetApi->delete_dag_asset_queued_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **before** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset**
> AssetResponse get_asset(asset_id)

Get Asset

Get an asset.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.asset_response import AssetResponse
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
    api_instance = airflow_client.client.AssetApi(api_client)
    asset_id = 56 # int | 

    try:
        # Get Asset
        api_response = api_instance.get_asset(asset_id)
        print("The response of AssetApi->get_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->get_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**|  | 

### Return type

[**AssetResponse**](AssetResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

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

# **get_asset_alias**
> object get_asset_alias(asset_alias_id)

Get Asset Alias

Get an asset alias.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
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
    api_instance = airflow_client.client.AssetApi(api_client)
    asset_alias_id = 56 # int | 

    try:
        # Get Asset Alias
        api_response = api_instance.get_asset_alias(asset_alias_id)
        print("The response of AssetApi->get_asset_alias:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->get_asset_alias: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_alias_id** | **int**|  | 

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

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

# **get_asset_aliases**
> AssetAliasCollectionResponse get_asset_aliases(limit=limit, offset=offset, name_pattern=name_pattern, order_by=order_by)

Get Asset Aliases

Get asset aliases.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.asset_alias_collection_response import AssetAliasCollectionResponse
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
    api_instance = airflow_client.client.AssetApi(api_client)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)
    name_pattern = 'name_pattern_example' # str |  (optional)
    order_by = 'id' # str |  (optional) (default to 'id')

    try:
        # Get Asset Aliases
        api_response = api_instance.get_asset_aliases(limit=limit, offset=offset, name_pattern=name_pattern, order_by=order_by)
        print("The response of AssetApi->get_asset_aliases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->get_asset_aliases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **name_pattern** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] [default to &#39;id&#39;]

### Return type

[**AssetAliasCollectionResponse**](AssetAliasCollectionResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

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

# **get_asset_events**
> AssetEventCollectionResponse get_asset_events(limit=limit, offset=offset, order_by=order_by, asset_id=asset_id, source_dag_id=source_dag_id, source_task_id=source_task_id, source_run_id=source_run_id, source_map_index=source_map_index, timestamp_gte=timestamp_gte, timestamp_lte=timestamp_lte)

Get Asset Events

Get asset events.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.asset_event_collection_response import AssetEventCollectionResponse
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
    api_instance = airflow_client.client.AssetApi(api_client)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)
    order_by = 'timestamp' # str |  (optional) (default to 'timestamp')
    asset_id = 56 # int |  (optional)
    source_dag_id = 'source_dag_id_example' # str |  (optional)
    source_task_id = 'source_task_id_example' # str |  (optional)
    source_run_id = 'source_run_id_example' # str |  (optional)
    source_map_index = 56 # int |  (optional)
    timestamp_gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    timestamp_lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Get Asset Events
        api_response = api_instance.get_asset_events(limit=limit, offset=offset, order_by=order_by, asset_id=asset_id, source_dag_id=source_dag_id, source_task_id=source_task_id, source_run_id=source_run_id, source_map_index=source_map_index, timestamp_gte=timestamp_gte, timestamp_lte=timestamp_lte)
        print("The response of AssetApi->get_asset_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->get_asset_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **order_by** | **str**|  | [optional] [default to &#39;timestamp&#39;]
 **asset_id** | **int**|  | [optional] 
 **source_dag_id** | **str**|  | [optional] 
 **source_task_id** | **str**|  | [optional] 
 **source_run_id** | **str**|  | [optional] 
 **source_map_index** | **int**|  | [optional] 
 **timestamp_gte** | **datetime**|  | [optional] 
 **timestamp_lte** | **datetime**|  | [optional] 

### Return type

[**AssetEventCollectionResponse**](AssetEventCollectionResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

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

# **get_asset_queued_events**
> QueuedEventCollectionResponse get_asset_queued_events(asset_id, before=before)

Get Asset Queued Events

Get queued asset events for an asset.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.queued_event_collection_response import QueuedEventCollectionResponse
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
    api_instance = airflow_client.client.AssetApi(api_client)
    asset_id = 56 # int | 
    before = 'before_example' # str |  (optional)

    try:
        # Get Asset Queued Events
        api_response = api_instance.get_asset_queued_events(asset_id, before=before)
        print("The response of AssetApi->get_asset_queued_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->get_asset_queued_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**|  | 
 **before** | **str**|  | [optional] 

### Return type

[**QueuedEventCollectionResponse**](QueuedEventCollectionResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

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

# **get_assets**
> AssetCollectionResponse get_assets(limit=limit, offset=offset, name_pattern=name_pattern, uri_pattern=uri_pattern, dag_ids=dag_ids, only_active=only_active, order_by=order_by)

Get Assets

Get assets.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.asset_collection_response import AssetCollectionResponse
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
    api_instance = airflow_client.client.AssetApi(api_client)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)
    name_pattern = 'name_pattern_example' # str |  (optional)
    uri_pattern = 'uri_pattern_example' # str |  (optional)
    dag_ids = ['dag_ids_example'] # List[str] |  (optional)
    only_active = True # bool |  (optional) (default to True)
    order_by = 'id' # str |  (optional) (default to 'id')

    try:
        # Get Assets
        api_response = api_instance.get_assets(limit=limit, offset=offset, name_pattern=name_pattern, uri_pattern=uri_pattern, dag_ids=dag_ids, only_active=only_active, order_by=order_by)
        print("The response of AssetApi->get_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->get_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **name_pattern** | **str**|  | [optional] 
 **uri_pattern** | **str**|  | [optional] 
 **dag_ids** | [**List[str]**](str.md)|  | [optional] 
 **only_active** | **bool**|  | [optional] [default to True]
 **order_by** | **str**|  | [optional] [default to &#39;id&#39;]

### Return type

[**AssetCollectionResponse**](AssetCollectionResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

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

# **get_dag_asset_queued_event**
> QueuedEventResponse get_dag_asset_queued_event(dag_id, asset_id, before=before)

Get Dag Asset Queued Event

Get a queued asset event for a DAG.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.queued_event_response import QueuedEventResponse
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
    api_instance = airflow_client.client.AssetApi(api_client)
    dag_id = 'dag_id_example' # str | 
    asset_id = 56 # int | 
    before = 'before_example' # str |  (optional)

    try:
        # Get Dag Asset Queued Event
        api_response = api_instance.get_dag_asset_queued_event(dag_id, asset_id, before=before)
        print("The response of AssetApi->get_dag_asset_queued_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->get_dag_asset_queued_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **asset_id** | **int**|  | 
 **before** | **str**|  | [optional] 

### Return type

[**QueuedEventResponse**](QueuedEventResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

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

# **get_dag_asset_queued_events**
> QueuedEventCollectionResponse get_dag_asset_queued_events(dag_id, before=before)

Get Dag Asset Queued Events

Get queued asset events for a DAG.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.queued_event_collection_response import QueuedEventCollectionResponse
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
    api_instance = airflow_client.client.AssetApi(api_client)
    dag_id = 'dag_id_example' # str | 
    before = 'before_example' # str |  (optional)

    try:
        # Get Dag Asset Queued Events
        api_response = api_instance.get_dag_asset_queued_events(dag_id, before=before)
        print("The response of AssetApi->get_dag_asset_queued_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->get_dag_asset_queued_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **before** | **str**|  | [optional] 

### Return type

[**QueuedEventCollectionResponse**](QueuedEventCollectionResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

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

# **materialize_asset**
> DAGRunResponse materialize_asset(asset_id)

Materialize Asset

Materialize an asset by triggering a DAG run that produces it.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.dag_run_response import DAGRunResponse
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
    api_instance = airflow_client.client.AssetApi(api_client)
    asset_id = 56 # int | 

    try:
        # Materialize Asset
        api_response = api_instance.materialize_asset(asset_id)
        print("The response of AssetApi->materialize_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->materialize_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**|  | 

### Return type

[**DAGRunResponse**](DAGRunResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

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
**409** | Conflict |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

