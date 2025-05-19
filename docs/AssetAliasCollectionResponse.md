# AssetAliasCollectionResponse

Asset alias collection response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_aliases** | [**List[AssetAliasResponse]**](AssetAliasResponse.md) |  | 
**total_entries** | **int** |  | 

## Example

```python
from airflow_client.client.models.asset_alias_collection_response import AssetAliasCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssetAliasCollectionResponse from a JSON string
asset_alias_collection_response_instance = AssetAliasCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(AssetAliasCollectionResponse.to_json())

# convert the object into a dict
asset_alias_collection_response_dict = asset_alias_collection_response_instance.to_dict()
# create an instance of AssetAliasCollectionResponse from a dict
asset_alias_collection_response_from_dict = AssetAliasCollectionResponse.from_dict(asset_alias_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


