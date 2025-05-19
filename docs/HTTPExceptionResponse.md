# HTTPExceptionResponse

HTTPException Model used for error response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | [**Detail**](Detail.md) |  | 

## Example

```python
from airflow_client.client.models.http_exception_response import HTTPExceptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HTTPExceptionResponse from a JSON string
http_exception_response_instance = HTTPExceptionResponse.from_json(json)
# print the JSON string representation of the object
print(HTTPExceptionResponse.to_json())

# convert the object into a dict
http_exception_response_dict = http_exception_response_instance.to_dict()
# create an instance of HTTPExceptionResponse from a dict
http_exception_response_from_dict = HTTPExceptionResponse.from_dict(http_exception_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


