# AppBuilderMenuItemResponse

Serializer for AppBuilder Menu Item responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from airflow_client.client.models.app_builder_menu_item_response import AppBuilderMenuItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppBuilderMenuItemResponse from a JSON string
app_builder_menu_item_response_instance = AppBuilderMenuItemResponse.from_json(json)
# print the JSON string representation of the object
print(AppBuilderMenuItemResponse.to_json())

# convert the object into a dict
app_builder_menu_item_response_dict = app_builder_menu_item_response_instance.to_dict()
# create an instance of AppBuilderMenuItemResponse from a dict
app_builder_menu_item_response_from_dict = AppBuilderMenuItemResponse.from_dict(app_builder_menu_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


