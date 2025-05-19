# PluginCollectionResponse

Plugin Collection serializer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plugins** | [**List[PluginResponse]**](PluginResponse.md) |  | 
**total_entries** | **int** |  | 

## Example

```python
from airflow_client.client.models.plugin_collection_response import PluginCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PluginCollectionResponse from a JSON string
plugin_collection_response_instance = PluginCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(PluginCollectionResponse.to_json())

# convert the object into a dict
plugin_collection_response_dict = plugin_collection_response_instance.to_dict()
# create an instance of PluginCollectionResponse from a dict
plugin_collection_response_from_dict = PluginCollectionResponse.from_dict(plugin_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


