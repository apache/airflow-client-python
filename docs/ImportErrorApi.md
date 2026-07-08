# airflow_client.client.ImportErrorApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_import_error**](ImportErrorApi.md#get_import_error) | **GET** /api/v2/importErrors/{import_error_id} | Get Import Error
[**get_import_errors**](ImportErrorApi.md#get_import_errors) | **GET** /api/v2/importErrors | Get Import Errors


# **get_import_error**
> ImportErrorResponse get_import_error(import_error_id)

Get Import Error

Get an import error.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

```python
import airflow_client.client
from airflow_client.client.models.import_error_response import ImportErrorResponse
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
    api_instance = airflow_client.client.ImportErrorApi(api_client)
    import_error_id = 56 # int | 

    try:
        # Get Import Error
        api_response = api_instance.get_import_error(import_error_id)
        print("The response of ImportErrorApi->get_import_error:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportErrorApi->get_import_error: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_error_id** | **int**|  | 

### Return type

[**ImportErrorResponse**](ImportErrorResponse.md)

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

# **get_import_errors**
> ImportErrorCollectionResponse get_import_errors(limit=limit, offset=offset, order_by=order_by, filename_pattern=filename_pattern, filename_prefix_pattern=filename_prefix_pattern, filename=filename, bundle_name=bundle_name)

Get Import Errors

Get all import errors.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer Authentication (HTTPBearer):

```python
import airflow_client.client
from airflow_client.client.models.import_error_collection_response import ImportErrorCollectionResponse
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
    api_instance = airflow_client.client.ImportErrorApi(api_client)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)
    order_by = ["id"] # List[str] | Attributes to order by, multi criteria sort is supported. Prefix with `-` for descending order. Supported attributes: `id, timestamp, filename, bundle_name, stacktrace, import_error_id` (optional) (default to ["id"])
    filename_pattern = 'filename_pattern_example' # str | SQL LIKE expression — use `%` / `_` wildcards (e.g. `%customer_%`). Use the pipe `|` operator for OR logic (e.g. `dag1 | dag2`). Regular expressions are **not** supported.   **Performance note:** this full-match pattern is evaluated as ``ILIKE '%term%'`` and most of the time prevents the database from using B-tree indexes, which can be very slow on large tables. Prefer the equivalent ``filename_prefix_pattern`` parameter when possible. (optional)
    filename_prefix_pattern = 'filename_prefix_pattern_example' # str | Prefix match — returns items whose value starts with the given string (case-sensitive, index-friendly). Use the pipe `|` operator for OR logic (e.g. `dag1|dag2`). Use `~` to match all. Wildcard characters (`%`, `_`) are treated as literal characters. Trailing non-alphanumeric characters in the prefix are stripped before matching so the range scan stays index-compatible under locale-aware collations — e.g. `test_` effectively matches items starting with `test`, and `s3://` matches items starting with `s3`. (optional)
    filename = 'filename_example' # str | Exact filename match. Returns only the import error for this specific file path. (optional)
    bundle_name = 'bundle_name_example' # str | Exact bundle name match. Returns only import errors from this specific bundle. (optional)

    try:
        # Get Import Errors
        api_response = api_instance.get_import_errors(limit=limit, offset=offset, order_by=order_by, filename_pattern=filename_pattern, filename_prefix_pattern=filename_prefix_pattern, filename=filename, bundle_name=bundle_name)
        print("The response of ImportErrorApi->get_import_errors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportErrorApi->get_import_errors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **order_by** | [**List[str]**](str.md)| Attributes to order by, multi criteria sort is supported. Prefix with &#x60;-&#x60; for descending order. Supported attributes: &#x60;id, timestamp, filename, bundle_name, stacktrace, import_error_id&#x60; | [optional] [default to [&quot;id&quot;]]
 **filename_pattern** | **str**| SQL LIKE expression — use &#x60;%&#x60; / &#x60;_&#x60; wildcards (e.g. &#x60;%customer_%&#x60;). Use the pipe &#x60;|&#x60; operator for OR logic (e.g. &#x60;dag1 | dag2&#x60;). Regular expressions are **not** supported.   **Performance note:** this full-match pattern is evaluated as &#x60;&#x60;ILIKE &#39;%term%&#39;&#x60;&#x60; and most of the time prevents the database from using B-tree indexes, which can be very slow on large tables. Prefer the equivalent &#x60;&#x60;filename_prefix_pattern&#x60;&#x60; parameter when possible. | [optional] 
 **filename_prefix_pattern** | **str**| Prefix match — returns items whose value starts with the given string (case-sensitive, index-friendly). Use the pipe &#x60;|&#x60; operator for OR logic (e.g. &#x60;dag1|dag2&#x60;). Use &#x60;~&#x60; to match all. Wildcard characters (&#x60;%&#x60;, &#x60;_&#x60;) are treated as literal characters. Trailing non-alphanumeric characters in the prefix are stripped before matching so the range scan stays index-compatible under locale-aware collations — e.g. &#x60;test_&#x60; effectively matches items starting with &#x60;test&#x60;, and &#x60;s3://&#x60; matches items starting with &#x60;s3&#x60;. | [optional] 
 **filename** | **str**| Exact filename match. Returns only the import error for this specific file path. | [optional] 
 **bundle_name** | **str**| Exact bundle name match. Returns only import errors from this specific bundle. | [optional] 

### Return type

[**ImportErrorCollectionResponse**](ImportErrorCollectionResponse.md)

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

