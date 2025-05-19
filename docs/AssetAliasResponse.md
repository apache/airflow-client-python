# AssetAliasResponse

Asset alias serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** |  | 
**id** | **int** |  | 
**name** | **str** |  | 

## Example

```python
from airflow_client.client.models.asset_alias_response import AssetAliasResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssetAliasResponse from a JSON string
asset_alias_response_instance = AssetAliasResponse.from_json(json)
# print the JSON string representation of the object
print(AssetAliasResponse.to_json())

# convert the object into a dict
asset_alias_response_dict = asset_alias_response_instance.to_dict()
# create an instance of AssetAliasResponse from a dict
asset_alias_response_from_dict = AssetAliasResponse.from_dict(asset_alias_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


