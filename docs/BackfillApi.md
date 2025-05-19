# airflow_client.client.BackfillApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_backfill**](BackfillApi.md#cancel_backfill) | **PUT** /api/v2/backfills/{backfill_id}/cancel | Cancel Backfill
[**create_backfill**](BackfillApi.md#create_backfill) | **POST** /api/v2/backfills | Create Backfill
[**create_backfill_dry_run**](BackfillApi.md#create_backfill_dry_run) | **POST** /api/v2/backfills/dry_run | Create Backfill Dry Run
[**get_backfill**](BackfillApi.md#get_backfill) | **GET** /api/v2/backfills/{backfill_id} | Get Backfill
[**list_backfills**](BackfillApi.md#list_backfills) | **GET** /api/v2/backfills | List Backfills
[**pause_backfill**](BackfillApi.md#pause_backfill) | **PUT** /api/v2/backfills/{backfill_id}/pause | Pause Backfill
[**unpause_backfill**](BackfillApi.md#unpause_backfill) | **PUT** /api/v2/backfills/{backfill_id}/unpause | Unpause Backfill


# **cancel_backfill**
> BackfillResponse cancel_backfill(backfill_id)

Cancel Backfill

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.backfill_response import BackfillResponse
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
    api_instance = airflow_client.client.BackfillApi(api_client)
    backfill_id = 56 # int | 

    try:
        # Cancel Backfill
        api_response = api_instance.cancel_backfill(backfill_id)
        print("The response of BackfillApi->cancel_backfill:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackfillApi->cancel_backfill: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backfill_id** | **int**|  | 

### Return type

[**BackfillResponse**](BackfillResponse.md)

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

# **create_backfill**
> BackfillResponse create_backfill(backfill_post_body)

Create Backfill

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.backfill_post_body import BackfillPostBody
from airflow_client.client.models.backfill_response import BackfillResponse
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
    api_instance = airflow_client.client.BackfillApi(api_client)
    backfill_post_body = airflow_client.client.BackfillPostBody() # BackfillPostBody | 

    try:
        # Create Backfill
        api_response = api_instance.create_backfill(backfill_post_body)
        print("The response of BackfillApi->create_backfill:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackfillApi->create_backfill: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backfill_post_body** | [**BackfillPostBody**](BackfillPostBody.md)|  | 

### Return type

[**BackfillResponse**](BackfillResponse.md)

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
**409** | Conflict |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_backfill_dry_run**
> DryRunBackfillCollectionResponse create_backfill_dry_run(backfill_post_body)

Create Backfill Dry Run

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.backfill_post_body import BackfillPostBody
from airflow_client.client.models.dry_run_backfill_collection_response import DryRunBackfillCollectionResponse
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
    api_instance = airflow_client.client.BackfillApi(api_client)
    backfill_post_body = airflow_client.client.BackfillPostBody() # BackfillPostBody | 

    try:
        # Create Backfill Dry Run
        api_response = api_instance.create_backfill_dry_run(backfill_post_body)
        print("The response of BackfillApi->create_backfill_dry_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackfillApi->create_backfill_dry_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backfill_post_body** | [**BackfillPostBody**](BackfillPostBody.md)|  | 

### Return type

[**DryRunBackfillCollectionResponse**](DryRunBackfillCollectionResponse.md)

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
**409** | Conflict |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_backfill**
> BackfillResponse get_backfill(backfill_id)

Get Backfill

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.backfill_response import BackfillResponse
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
    api_instance = airflow_client.client.BackfillApi(api_client)
    backfill_id = 56 # int | 

    try:
        # Get Backfill
        api_response = api_instance.get_backfill(backfill_id)
        print("The response of BackfillApi->get_backfill:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackfillApi->get_backfill: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backfill_id** | **int**|  | 

### Return type

[**BackfillResponse**](BackfillResponse.md)

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

# **list_backfills**
> BackfillCollectionResponse list_backfills(dag_id, limit=limit, offset=offset, order_by=order_by)

List Backfills

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.backfill_collection_response import BackfillCollectionResponse
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
    api_instance = airflow_client.client.BackfillApi(api_client)
    dag_id = 'dag_id_example' # str | 
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)
    order_by = 'id' # str |  (optional) (default to 'id')

    try:
        # List Backfills
        api_response = api_instance.list_backfills(dag_id, limit=limit, offset=offset, order_by=order_by)
        print("The response of BackfillApi->list_backfills:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackfillApi->list_backfills: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **order_by** | **str**|  | [optional] [default to &#39;id&#39;]

### Return type

[**BackfillCollectionResponse**](BackfillCollectionResponse.md)

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pause_backfill**
> BackfillResponse pause_backfill(backfill_id)

Pause Backfill

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.backfill_response import BackfillResponse
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
    api_instance = airflow_client.client.BackfillApi(api_client)
    backfill_id = 56 # int | 

    try:
        # Pause Backfill
        api_response = api_instance.pause_backfill(backfill_id)
        print("The response of BackfillApi->pause_backfill:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackfillApi->pause_backfill: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backfill_id** | **int**|  | 

### Return type

[**BackfillResponse**](BackfillResponse.md)

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

# **unpause_backfill**
> BackfillResponse unpause_backfill(backfill_id)

Unpause Backfill

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.backfill_response import BackfillResponse
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
    api_instance = airflow_client.client.BackfillApi(api_client)
    backfill_id = 56 # int | 

    try:
        # Unpause Backfill
        api_response = api_instance.unpause_backfill(backfill_id)
        print("The response of BackfillApi->unpause_backfill:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackfillApi->unpause_backfill: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backfill_id** | **int**|  | 

### Return type

[**BackfillResponse**](BackfillResponse.md)

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

