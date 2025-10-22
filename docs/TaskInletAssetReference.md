# TaskInletAssetReference

Task inlet reference serializer for assets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**dag_id** | **str** |  | 
**task_id** | **str** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from airflow_client.client.models.task_inlet_asset_reference import TaskInletAssetReference

# TODO update the JSON string below
json = "{}"
# create an instance of TaskInletAssetReference from a JSON string
task_inlet_asset_reference_instance = TaskInletAssetReference.from_json(json)
# print the JSON string representation of the object
print(TaskInletAssetReference.to_json())

# convert the object into a dict
task_inlet_asset_reference_dict = task_inlet_asset_reference_instance.to_dict()
# create an instance of TaskInletAssetReference from a dict
task_inlet_asset_reference_from_dict = TaskInletAssetReference.from_dict(task_inlet_asset_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


