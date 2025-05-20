# AssetResponse

Asset serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliases** | [**List[AssetAliasResponse]**](AssetAliasResponse.md) |  | 
**consuming_dags** | [**List[DagScheduleAssetReference]**](DagScheduleAssetReference.md) |  | 
**created_at** | **datetime** |  | 
**extra** | **object** |  | [optional] 
**group** | **str** |  | 
**id** | **int** |  | 
**name** | **str** |  | 
**producing_tasks** | [**List[TaskOutletAssetReference]**](TaskOutletAssetReference.md) |  | 
**updated_at** | **datetime** |  | 
**uri** | **str** |  | 

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


