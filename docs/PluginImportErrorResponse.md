# PluginImportErrorResponse

Plugin Import Error serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | 
**source** | **str** |  | 

## Example

```python
from airflow_client.client.models.plugin_import_error_response import PluginImportErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PluginImportErrorResponse from a JSON string
plugin_import_error_response_instance = PluginImportErrorResponse.from_json(json)
# print the JSON string representation of the object
print(PluginImportErrorResponse.to_json())

# convert the object into a dict
plugin_import_error_response_dict = plugin_import_error_response_instance.to_dict()
# create an instance of PluginImportErrorResponse from a dict
plugin_import_error_response_from_dict = PluginImportErrorResponse.from_dict(plugin_import_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


