# PluginImportErrorCollectionResponse

Plugin Import Error Collection serializer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**import_errors** | [**List[PluginImportErrorResponse]**](PluginImportErrorResponse.md) |  | 
**total_entries** | **int** |  | 

## Example

```python
from airflow_client.client.models.plugin_import_error_collection_response import PluginImportErrorCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PluginImportErrorCollectionResponse from a JSON string
plugin_import_error_collection_response_instance = PluginImportErrorCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(PluginImportErrorCollectionResponse.to_json())

# convert the object into a dict
plugin_import_error_collection_response_dict = plugin_import_error_collection_response_instance.to_dict()
# create an instance of PluginImportErrorCollectionResponse from a dict
plugin_import_error_collection_response_from_dict = PluginImportErrorCollectionResponse.from_dict(plugin_import_error_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


