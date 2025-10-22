# airflow_client.client.DAGApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_dag**](DAGApi.md#delete_dag) | **DELETE** /api/v2/dags/{dag_id} | Delete Dag
[**favorite_dag**](DAGApi.md#favorite_dag) | **POST** /api/v2/dags/{dag_id}/favorite | Favorite Dag
[**get_dag**](DAGApi.md#get_dag) | **GET** /api/v2/dags/{dag_id} | Get Dag
[**get_dag_details**](DAGApi.md#get_dag_details) | **GET** /api/v2/dags/{dag_id}/details | Get Dag Details
[**get_dag_tags**](DAGApi.md#get_dag_tags) | **GET** /api/v2/dagTags | Get Dag Tags
[**get_dags**](DAGApi.md#get_dags) | **GET** /api/v2/dags | Get Dags
[**patch_dag**](DAGApi.md#patch_dag) | **PATCH** /api/v2/dags/{dag_id} | Patch Dag
[**patch_dags**](DAGApi.md#patch_dags) | **PATCH** /api/v2/dags | Patch Dags
[**unfavorite_dag**](DAGApi.md#unfavorite_dag) | **POST** /api/v2/dags/{dag_id}/unfavorite | Unfavorite Dag


# **delete_dag**
> object delete_dag(dag_id)

Delete Dag

Delete the specific DAG.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

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

# Configure Bearer authorization: HTTPBearer
configuration = airflow_client.client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = airflow_client.client.DAGApi(api_client)
    dag_id = 'dag_id_example' # str | 

    try:
        # Delete Dag
        api_response = api_instance.delete_dag(dag_id)
        print("The response of DAGApi->delete_dag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DAGApi->delete_dag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [HTTPBearer](../README.md#HTTPBearer)

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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **favorite_dag**
> favorite_dag(dag_id)

Favorite Dag

Mark the DAG as favorite.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

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

# Configure Bearer authorization: HTTPBearer
configuration = airflow_client.client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = airflow_client.client.DAGApi(api_client)
    dag_id = 'dag_id_example' # str | 

    try:
        # Favorite Dag
        api_instance.favorite_dag(dag_id)
    except Exception as e:
        print("Exception when calling DAGApi->favorite_dag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [HTTPBearer](../README.md#HTTPBearer)

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

# **get_dag**
> DAGResponse get_dag(dag_id)

Get Dag

Get basic information about a DAG.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

```python
import airflow_client.client
from airflow_client.client.models.dag_response import DAGResponse
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
    api_instance = airflow_client.client.DAGApi(api_client)
    dag_id = 'dag_id_example' # str | 

    try:
        # Get Dag
        api_response = api_instance.get_dag(dag_id)
        print("The response of DAGApi->get_dag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DAGApi->get_dag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 

### Return type

[**DAGResponse**](DAGResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [HTTPBearer](../README.md#HTTPBearer)

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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dag_details**
> DAGDetailsResponse get_dag_details(dag_id)

Get Dag Details

Get details of DAG.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

```python
import airflow_client.client
from airflow_client.client.models.dag_details_response import DAGDetailsResponse
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
    api_instance = airflow_client.client.DAGApi(api_client)
    dag_id = 'dag_id_example' # str | 

    try:
        # Get Dag Details
        api_response = api_instance.get_dag_details(dag_id)
        print("The response of DAGApi->get_dag_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DAGApi->get_dag_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 

### Return type

[**DAGDetailsResponse**](DAGDetailsResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [HTTPBearer](../README.md#HTTPBearer)

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
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dag_tags**
> DAGTagCollectionResponse get_dag_tags(limit=limit, offset=offset, order_by=order_by, tag_name_pattern=tag_name_pattern)

Get Dag Tags

Get all DAG tags.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

```python
import airflow_client.client
from airflow_client.client.models.dag_tag_collection_response import DAGTagCollectionResponse
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
    api_instance = airflow_client.client.DAGApi(api_client)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)
    order_by = ["name"] # List[str] |  (optional) (default to ["name"])
    tag_name_pattern = 'tag_name_pattern_example' # str | SQL LIKE expression — use `%` / `_` wildcards (e.g. `%customer_%`). Regular expressions are **not** supported. (optional)

    try:
        # Get Dag Tags
        api_response = api_instance.get_dag_tags(limit=limit, offset=offset, order_by=order_by, tag_name_pattern=tag_name_pattern)
        print("The response of DAGApi->get_dag_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DAGApi->get_dag_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **order_by** | [**List[str]**](str.md)|  | [optional] [default to [&quot;name&quot;]]
 **tag_name_pattern** | **str**| SQL LIKE expression — use &#x60;%&#x60; / &#x60;_&#x60; wildcards (e.g. &#x60;%customer_%&#x60;). Regular expressions are **not** supported. | [optional] 

### Return type

[**DAGTagCollectionResponse**](DAGTagCollectionResponse.md)

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

# **get_dags**
> DAGCollectionResponse get_dags(limit=limit, offset=offset, tags=tags, tags_match_mode=tags_match_mode, owners=owners, dag_id_pattern=dag_id_pattern, dag_display_name_pattern=dag_display_name_pattern, exclude_stale=exclude_stale, paused=paused, has_import_errors=has_import_errors, last_dag_run_state=last_dag_run_state, bundle_name=bundle_name, bundle_version=bundle_version, has_asset_schedule=has_asset_schedule, asset_dependency=asset_dependency, dag_run_start_date_gte=dag_run_start_date_gte, dag_run_start_date_gt=dag_run_start_date_gt, dag_run_start_date_lte=dag_run_start_date_lte, dag_run_start_date_lt=dag_run_start_date_lt, dag_run_end_date_gte=dag_run_end_date_gte, dag_run_end_date_gt=dag_run_end_date_gt, dag_run_end_date_lte=dag_run_end_date_lte, dag_run_end_date_lt=dag_run_end_date_lt, dag_run_state=dag_run_state, order_by=order_by, is_favorite=is_favorite)

Get Dags

Get all DAGs.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

```python
import airflow_client.client
from airflow_client.client.models.dag_collection_response import DAGCollectionResponse
from airflow_client.client.models.dag_run_state import DagRunState
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
    api_instance = airflow_client.client.DAGApi(api_client)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)
    tags = ['tags_example'] # List[str] |  (optional)
    tags_match_mode = 'tags_match_mode_example' # str |  (optional)
    owners = ['owners_example'] # List[str] |  (optional)
    dag_id_pattern = 'dag_id_pattern_example' # str | SQL LIKE expression — use `%` / `_` wildcards (e.g. `%customer_%`). Regular expressions are **not** supported. (optional)
    dag_display_name_pattern = 'dag_display_name_pattern_example' # str | SQL LIKE expression — use `%` / `_` wildcards (e.g. `%customer_%`). Regular expressions are **not** supported. (optional)
    exclude_stale = True # bool |  (optional) (default to True)
    paused = True # bool |  (optional)
    has_import_errors = True # bool | Filter Dags by having import errors. Only Dags that have been successfully loaded before will be returned. (optional)
    last_dag_run_state = airflow_client.client.DagRunState() # DagRunState |  (optional)
    bundle_name = 'bundle_name_example' # str |  (optional)
    bundle_version = 'bundle_version_example' # str |  (optional)
    has_asset_schedule = True # bool | Filter Dags with asset-based scheduling (optional)
    asset_dependency = 'asset_dependency_example' # str | Filter Dags by asset dependency (name or URI) (optional)
    dag_run_start_date_gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    dag_run_start_date_gt = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    dag_run_start_date_lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    dag_run_start_date_lt = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    dag_run_end_date_gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    dag_run_end_date_gt = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    dag_run_end_date_lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    dag_run_end_date_lt = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    dag_run_state = ['dag_run_state_example'] # List[str] |  (optional)
    order_by = [dag_id] # List[str] |  (optional) (default to [dag_id])
    is_favorite = True # bool |  (optional)

    try:
        # Get Dags
        api_response = api_instance.get_dags(limit=limit, offset=offset, tags=tags, tags_match_mode=tags_match_mode, owners=owners, dag_id_pattern=dag_id_pattern, dag_display_name_pattern=dag_display_name_pattern, exclude_stale=exclude_stale, paused=paused, has_import_errors=has_import_errors, last_dag_run_state=last_dag_run_state, bundle_name=bundle_name, bundle_version=bundle_version, has_asset_schedule=has_asset_schedule, asset_dependency=asset_dependency, dag_run_start_date_gte=dag_run_start_date_gte, dag_run_start_date_gt=dag_run_start_date_gt, dag_run_start_date_lte=dag_run_start_date_lte, dag_run_start_date_lt=dag_run_start_date_lt, dag_run_end_date_gte=dag_run_end_date_gte, dag_run_end_date_gt=dag_run_end_date_gt, dag_run_end_date_lte=dag_run_end_date_lte, dag_run_end_date_lt=dag_run_end_date_lt, dag_run_state=dag_run_state, order_by=order_by, is_favorite=is_favorite)
        print("The response of DAGApi->get_dags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DAGApi->get_dags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **tags** | [**List[str]**](str.md)|  | [optional] 
 **tags_match_mode** | **str**|  | [optional] 
 **owners** | [**List[str]**](str.md)|  | [optional] 
 **dag_id_pattern** | **str**| SQL LIKE expression — use &#x60;%&#x60; / &#x60;_&#x60; wildcards (e.g. &#x60;%customer_%&#x60;). Regular expressions are **not** supported. | [optional] 
 **dag_display_name_pattern** | **str**| SQL LIKE expression — use &#x60;%&#x60; / &#x60;_&#x60; wildcards (e.g. &#x60;%customer_%&#x60;). Regular expressions are **not** supported. | [optional] 
 **exclude_stale** | **bool**|  | [optional] [default to True]
 **paused** | **bool**|  | [optional] 
 **has_import_errors** | **bool**| Filter Dags by having import errors. Only Dags that have been successfully loaded before will be returned. | [optional] 
 **last_dag_run_state** | [**DagRunState**](.md)|  | [optional] 
 **bundle_name** | **str**|  | [optional] 
 **bundle_version** | **str**|  | [optional] 
 **has_asset_schedule** | **bool**| Filter Dags with asset-based scheduling | [optional] 
 **asset_dependency** | **str**| Filter Dags by asset dependency (name or URI) | [optional] 
 **dag_run_start_date_gte** | **datetime**|  | [optional] 
 **dag_run_start_date_gt** | **datetime**|  | [optional] 
 **dag_run_start_date_lte** | **datetime**|  | [optional] 
 **dag_run_start_date_lt** | **datetime**|  | [optional] 
 **dag_run_end_date_gte** | **datetime**|  | [optional] 
 **dag_run_end_date_gt** | **datetime**|  | [optional] 
 **dag_run_end_date_lte** | **datetime**|  | [optional] 
 **dag_run_end_date_lt** | **datetime**|  | [optional] 
 **dag_run_state** | [**List[str]**](str.md)|  | [optional] 
 **order_by** | [**List[str]**](str.md)|  | [optional] [default to [dag_id]]
 **is_favorite** | **bool**|  | [optional] 

### Return type

[**DAGCollectionResponse**](DAGCollectionResponse.md)

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

# **patch_dag**
> DAGResponse patch_dag(dag_id, dag_patch_body, update_mask=update_mask)

Patch Dag

Patch the specific DAG.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

```python
import airflow_client.client
from airflow_client.client.models.dag_patch_body import DAGPatchBody
from airflow_client.client.models.dag_response import DAGResponse
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
    api_instance = airflow_client.client.DAGApi(api_client)
    dag_id = 'dag_id_example' # str | 
    dag_patch_body = airflow_client.client.DAGPatchBody() # DAGPatchBody | 
    update_mask = ['update_mask_example'] # List[str] |  (optional)

    try:
        # Patch Dag
        api_response = api_instance.patch_dag(dag_id, dag_patch_body, update_mask=update_mask)
        print("The response of DAGApi->patch_dag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DAGApi->patch_dag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 
 **dag_patch_body** | [**DAGPatchBody**](DAGPatchBody.md)|  | 
 **update_mask** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**DAGResponse**](DAGResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [HTTPBearer](../README.md#HTTPBearer)

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

# **patch_dags**
> DAGCollectionResponse patch_dags(dag_patch_body, update_mask=update_mask, limit=limit, offset=offset, tags=tags, tags_match_mode=tags_match_mode, owners=owners, dag_id_pattern=dag_id_pattern, exclude_stale=exclude_stale, paused=paused)

Patch Dags

Patch multiple DAGs.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

```python
import airflow_client.client
from airflow_client.client.models.dag_collection_response import DAGCollectionResponse
from airflow_client.client.models.dag_patch_body import DAGPatchBody
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
    api_instance = airflow_client.client.DAGApi(api_client)
    dag_patch_body = airflow_client.client.DAGPatchBody() # DAGPatchBody | 
    update_mask = ['update_mask_example'] # List[str] |  (optional)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)
    tags = ['tags_example'] # List[str] |  (optional)
    tags_match_mode = 'tags_match_mode_example' # str |  (optional)
    owners = ['owners_example'] # List[str] |  (optional)
    dag_id_pattern = 'dag_id_pattern_example' # str | SQL LIKE expression — use `%` / `_` wildcards (e.g. `%customer_%`). Regular expressions are **not** supported. (optional)
    exclude_stale = True # bool |  (optional) (default to True)
    paused = True # bool |  (optional)

    try:
        # Patch Dags
        api_response = api_instance.patch_dags(dag_patch_body, update_mask=update_mask, limit=limit, offset=offset, tags=tags, tags_match_mode=tags_match_mode, owners=owners, dag_id_pattern=dag_id_pattern, exclude_stale=exclude_stale, paused=paused)
        print("The response of DAGApi->patch_dags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DAGApi->patch_dags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_patch_body** | [**DAGPatchBody**](DAGPatchBody.md)|  | 
 **update_mask** | [**List[str]**](str.md)|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **tags** | [**List[str]**](str.md)|  | [optional] 
 **tags_match_mode** | **str**|  | [optional] 
 **owners** | [**List[str]**](str.md)|  | [optional] 
 **dag_id_pattern** | **str**| SQL LIKE expression — use &#x60;%&#x60; / &#x60;_&#x60; wildcards (e.g. &#x60;%customer_%&#x60;). Regular expressions are **not** supported. | [optional] 
 **exclude_stale** | **bool**|  | [optional] [default to True]
 **paused** | **bool**|  | [optional] 

### Return type

[**DAGCollectionResponse**](DAGCollectionResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [HTTPBearer](../README.md#HTTPBearer)

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

# **unfavorite_dag**
> unfavorite_dag(dag_id)

Unfavorite Dag

Unmark the DAG as favorite.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

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

# Configure Bearer authorization: HTTPBearer
configuration = airflow_client.client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = airflow_client.client.DAGApi(api_client)
    dag_id = 'dag_id_example' # str | 

    try:
        # Unfavorite Dag
        api_instance.unfavorite_dag(dag_id)
    except Exception as e:
        print("Exception when calling DAGApi->unfavorite_dag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [HTTPBearer](../README.md#HTTPBearer)

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
**409** | Conflict |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

