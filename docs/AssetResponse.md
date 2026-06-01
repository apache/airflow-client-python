# AssetResponse

Asset serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**uri** | **str** |  | 
**group** | **str** |  | 
**extra** | **Dict[str, object]** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**scheduled_dags** | [**List[DagScheduleAssetReference]**](DagScheduleAssetReference.md) |  | 
**producing_tasks** | [**List[TaskOutletAssetReference]**](TaskOutletAssetReference.md) |  | 
**consuming_tasks** | [**List[TaskInletAssetReference]**](TaskInletAssetReference.md) |  | 
**aliases** | [**List[AssetAliasResponse]**](AssetAliasResponse.md) |  | 
**watchers** | [**List[AssetWatcherResponse]**](AssetWatcherResponse.md) |  | 
**last_asset_event** | [**LastAssetEventResponse**](LastAssetEventResponse.md) |  | [optional] 

## Example

```python
from airflow_client.client.models.asset_response import AssetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssetResponse from a JSON string
asset_response_instance = AssetResponse.from_json(json)
# print the JSON string representation of the object
print(AssetResponse.to_json())

# convert the object into a dict
asset_response_dict = asset_response_instance.to_dict()
# create an instance of AssetResponse from a dict
asset_response_from_dict = AssetResponse.from_dict(asset_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


