# AssetEventResponse

Asset event serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **int** |  | 
**created_dagruns** | [**List[DagRunAssetReference]**](DagRunAssetReference.md) |  | 
**extra** | **object** |  | [optional] 
**group** | **str** |  | [optional] 
**id** | **int** |  | 
**name** | **str** |  | [optional] 
**source_dag_id** | **str** |  | [optional] 
**source_map_index** | **int** |  | 
**source_run_id** | **str** |  | [optional] 
**source_task_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | 
**uri** | **str** |  | [optional] 

## Example

```python
from airflow_client.client.models.asset_event_response import AssetEventResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssetEventResponse from a JSON string
asset_event_response_instance = AssetEventResponse.from_json(json)
# print the JSON string representation of the object
print(AssetEventResponse.to_json())

# convert the object into a dict
asset_event_response_dict = asset_event_response_instance.to_dict()
# create an instance of AssetEventResponse from a dict
asset_event_response_from_dict = AssetEventResponse.from_dict(asset_event_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


