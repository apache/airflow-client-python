# AppBuilderViewResponse

Serializer for AppBuilder View responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**view** | **str** |  | [optional] 

## Example

```python
from airflow_client.client.models.app_builder_view_response import AppBuilderViewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppBuilderViewResponse from a JSON string
app_builder_view_response_instance = AppBuilderViewResponse.from_json(json)
# print the JSON string representation of the object
print(AppBuilderViewResponse.to_json())

# convert the object into a dict
app_builder_view_response_dict = app_builder_view_response_instance.to_dict()
# create an instance of AppBuilderViewResponse from a dict
app_builder_view_response_from_dict = AppBuilderViewResponse.from_dict(app_builder_view_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


