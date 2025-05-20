# airflow_client.client.PoolApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_pools**](PoolApi.md#bulk_pools) | **PATCH** /api/v2/pools | Bulk Pools
[**delete_pool**](PoolApi.md#delete_pool) | **DELETE** /api/v2/pools/{pool_name} | Delete Pool
[**get_pool**](PoolApi.md#get_pool) | **GET** /api/v2/pools/{pool_name} | Get Pool
[**get_pools**](PoolApi.md#get_pools) | **GET** /api/v2/pools | Get Pools
[**patch_pool**](PoolApi.md#patch_pool) | **PATCH** /api/v2/pools/{pool_name} | Patch Pool
[**post_pool**](PoolApi.md#post_pool) | **POST** /api/v2/pools | Post Pool


# **bulk_pools**
> BulkResponse bulk_pools(bulk_body_pool_body)

Bulk Pools

Bulk create, update, and delete pools.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.bulk_body_pool_body import BulkBodyPoolBody
from airflow_client.client.models.bulk_response import BulkResponse
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
    api_instance = airflow_client.client.PoolApi(api_client)
    bulk_body_pool_body = airflow_client.client.BulkBodyPoolBody() # BulkBodyPoolBody | 

    try:
        # Bulk Pools
        api_response = api_instance.bulk_pools(bulk_body_pool_body)
        print("The response of PoolApi->bulk_pools:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoolApi->bulk_pools: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_body_pool_body** | [**BulkBodyPoolBody**](BulkBodyPoolBody.md)|  | 

### Return type

[**BulkResponse**](BulkResponse.md)

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pool**
> delete_pool(pool_name)

Delete Pool

Delete a pool entry.

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
    api_instance = airflow_client.client.PoolApi(api_client)
    pool_name = 'pool_name_example' # str | 

    try:
        # Delete Pool
        api_instance.delete_pool(pool_name)
    except Exception as e:
        print("Exception when calling PoolApi->delete_pool: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_name** | **str**|  | 

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

# **get_pool**
> PoolResponse get_pool(pool_name)

Get Pool

Get a pool.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.pool_response import PoolResponse
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
    api_instance = airflow_client.client.PoolApi(api_client)
    pool_name = 'pool_name_example' # str | 

    try:
        # Get Pool
        api_response = api_instance.get_pool(pool_name)
        print("The response of PoolApi->get_pool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoolApi->get_pool: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_name** | **str**|  | 

### Return type

[**PoolResponse**](PoolResponse.md)

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

# **get_pools**
> PoolCollectionResponse get_pools(limit=limit, offset=offset, order_by=order_by, pool_name_pattern=pool_name_pattern)

Get Pools

Get all pools entries.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.pool_collection_response import PoolCollectionResponse
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
    api_instance = airflow_client.client.PoolApi(api_client)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)
    order_by = 'id' # str |  (optional) (default to 'id')
    pool_name_pattern = 'pool_name_pattern_example' # str |  (optional)

    try:
        # Get Pools
        api_response = api_instance.get_pools(limit=limit, offset=offset, order_by=order_by, pool_name_pattern=pool_name_pattern)
        print("The response of PoolApi->get_pools:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoolApi->get_pools: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **order_by** | **str**|  | [optional] [default to &#39;id&#39;]
 **pool_name_pattern** | **str**|  | [optional] 

### Return type

[**PoolCollectionResponse**](PoolCollectionResponse.md)

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

# **patch_pool**
> PoolResponse patch_pool(pool_name, pool_patch_body, update_mask=update_mask)

Patch Pool

Update a Pool.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.pool_patch_body import PoolPatchBody
from airflow_client.client.models.pool_response import PoolResponse
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
    api_instance = airflow_client.client.PoolApi(api_client)
    pool_name = 'pool_name_example' # str | 
    pool_patch_body = airflow_client.client.PoolPatchBody() # PoolPatchBody | 
    update_mask = ['update_mask_example'] # List[str] |  (optional)

    try:
        # Patch Pool
        api_response = api_instance.patch_pool(pool_name, pool_patch_body, update_mask=update_mask)
        print("The response of PoolApi->patch_pool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoolApi->patch_pool: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_name** | **str**|  | 
 **pool_patch_body** | [**PoolPatchBody**](PoolPatchBody.md)|  | 
 **update_mask** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**PoolResponse**](PoolResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_pool**
> PoolResponse post_pool(pool_body)

Post Pool

Create a Pool.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import airflow_client.client
from airflow_client.client.models.pool_body import PoolBody
from airflow_client.client.models.pool_response import PoolResponse
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
    api_instance = airflow_client.client.PoolApi(api_client)
    pool_body = airflow_client.client.PoolBody() # PoolBody | 

    try:
        # Post Pool
        api_response = api_instance.post_pool(pool_body)
        print("The response of PoolApi->post_pool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoolApi->post_pool: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_body** | [**PoolBody**](PoolBody.md)|  | 

### Return type

[**PoolResponse**](PoolResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**409** | Conflict |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

