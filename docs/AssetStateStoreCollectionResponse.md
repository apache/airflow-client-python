# AssetStateStoreCollectionResponse

All asset state store entries for an asset.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_state_store** | [**List[AssetStateStoreResponse]**](AssetStateStoreResponse.md) |  | 
**total_entries** | **int** |  | 

## Example

```python
from airflow_client.client.models.asset_state_store_collection_response import AssetStateStoreCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssetStateStoreCollectionResponse from a JSON string
asset_state_store_collection_response_instance = AssetStateStoreCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(AssetStateStoreCollectionResponse.to_json())

# convert the object into a dict
asset_state_store_collection_response_dict = asset_state_store_collection_response_instance.to_dict()
# create an instance of AssetStateStoreCollectionResponse from a dict
asset_state_store_collection_response_from_dict = AssetStateStoreCollectionResponse.from_dict(asset_state_store_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


