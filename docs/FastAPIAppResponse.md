# FastAPIAppResponse

Serializer for Plugin FastAPI App responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | **str** |  | 
**name** | **str** |  | 
**url_prefix** | **str** |  | 

## Example

```python
from airflow_client.client.models.fast_api_app_response import FastAPIAppResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FastAPIAppResponse from a JSON string
fast_api_app_response_instance = FastAPIAppResponse.from_json(json)
# print the JSON string representation of the object
print(FastAPIAppResponse.to_json())

# convert the object into a dict
fast_api_app_response_dict = fast_api_app_response_instance.to_dict()
# create an instance of FastAPIAppResponse from a dict
fast_api_app_response_from_dict = FastAPIAppResponse.from_dict(fast_api_app_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


