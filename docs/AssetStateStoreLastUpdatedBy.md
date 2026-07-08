# AssetStateStoreLastUpdatedBy

Writer info for the last write to an asset state store entry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_id** | **str** |  | [optional] 
**kind** | [**AssetStateStoreWriterKind**](AssetStateStoreWriterKind.md) |  | 
**map_index** | **int** |  | [optional] 
**run_id** | **str** |  | [optional] 
**task_id** | **str** |  | [optional] 

## Example

```python
from airflow_client.client.models.asset_state_store_last_updated_by import AssetStateStoreLastUpdatedBy

# TODO update the JSON string below
json = "{}"
# create an instance of AssetStateStoreLastUpdatedBy from a JSON string
asset_state_store_last_updated_by_instance = AssetStateStoreLastUpdatedBy.from_json(json)
# print the JSON string representation of the object
print(AssetStateStoreLastUpdatedBy.to_json())

# convert the object into a dict
asset_state_store_last_updated_by_dict = asset_state_store_last_updated_by_instance.to_dict()
# create an instance of AssetStateStoreLastUpdatedBy from a dict
asset_state_store_last_updated_by_from_dict = AssetStateStoreLastUpdatedBy.from_dict(asset_state_store_last_updated_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


