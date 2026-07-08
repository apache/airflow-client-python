# AssetStateStoreBody

Request body for setting an asset state store value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **object** |  | 

## Example

```python
from airflow_client.client.models.asset_state_store_body import AssetStateStoreBody

# TODO update the JSON string below
json = "{}"
# create an instance of AssetStateStoreBody from a JSON string
asset_state_store_body_instance = AssetStateStoreBody.from_json(json)
# print the JSON string representation of the object
print(AssetStateStoreBody.to_json())

# convert the object into a dict
asset_state_store_body_dict = asset_state_store_body_instance.to_dict()
# create an instance of AssetStateStoreBody from a dict
asset_state_store_body_from_dict = AssetStateStoreBody.from_dict(asset_state_store_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


