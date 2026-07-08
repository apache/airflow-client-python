# AssetStateStoreResponse

A single asset state store key/value pair with metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**last_updated_by** | [**AssetStateStoreLastUpdatedBy**](AssetStateStoreLastUpdatedBy.md) |  | [optional] 
**updated_at** | **datetime** |  | 
**value** | **object** |  | 

## Example

```python
from airflow_client.client.models.asset_state_store_response import AssetStateStoreResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssetStateStoreResponse from a JSON string
asset_state_store_response_instance = AssetStateStoreResponse.from_json(json)
# print the JSON string representation of the object
print(AssetStateStoreResponse.to_json())

# convert the object into a dict
asset_state_store_response_dict = asset_state_store_response_instance.to_dict()
# create an instance of AssetStateStoreResponse from a dict
asset_state_store_response_from_dict = AssetStateStoreResponse.from_dict(asset_state_store_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


