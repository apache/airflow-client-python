# PluginResponse

Plugin serializer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appbuilder_menu_items** | [**List[AppBuilderMenuItemResponse]**](AppBuilderMenuItemResponse.md) |  | 
**appbuilder_views** | [**List[AppBuilderViewResponse]**](AppBuilderViewResponse.md) |  | 
**fastapi_apps** | [**List[FastAPIAppResponse]**](FastAPIAppResponse.md) |  | 
**fastapi_root_middlewares** | [**List[FastAPIRootMiddlewareResponse]**](FastAPIRootMiddlewareResponse.md) |  | 
**flask_blueprints** | **List[str]** |  | 
**global_operator_extra_links** | **List[str]** |  | 
**listeners** | **List[str]** |  | 
**macros** | **List[str]** |  | 
**name** | **str** |  | 
**operator_extra_links** | **List[str]** |  | 
**source** | **str** |  | 
**timetables** | **List[str]** |  | 

## Example

```python
from airflow_client.client.models.plugin_response import PluginResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PluginResponse from a JSON string
plugin_response_instance = PluginResponse.from_json(json)
# print the JSON string representation of the object
print(PluginResponse.to_json())

# convert the object into a dict
plugin_response_dict = plugin_response_instance.to_dict()
# create an instance of PluginResponse from a dict
plugin_response_from_dict = PluginResponse.from_dict(plugin_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


