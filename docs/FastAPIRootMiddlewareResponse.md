# FastAPIRootMiddlewareResponse

Serializer for Plugin FastAPI root middleware responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**middleware** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from airflow_client.client.models.fast_api_root_middleware_response import FastAPIRootMiddlewareResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FastAPIRootMiddlewareResponse from a JSON string
fast_api_root_middleware_response_instance = FastAPIRootMiddlewareResponse.from_json(json)
# print the JSON string representation of the object
print(FastAPIRootMiddlewareResponse.to_json())

# convert the object into a dict
fast_api_root_middleware_response_dict = fast_api_root_middleware_response_instance.to_dict()
# create an instance of FastAPIRootMiddlewareResponse from a dict
fast_api_root_middleware_response_from_dict = FastAPIRootMiddlewareResponse.from_dict(fast_api_root_middleware_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


