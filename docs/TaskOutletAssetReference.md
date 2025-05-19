# TaskOutletAssetReference

Task outlet reference serializer for assets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**dag_id** | **str** |  | 
**task_id** | **str** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from airflow_client.client.models.task_outlet_asset_reference import TaskOutletAssetReference

# TODO update the JSON string below
json = "{}"
# create an instance of TaskOutletAssetReference from a JSON string
task_outlet_asset_reference_instance = TaskOutletAssetReference.from_json(json)
# print the JSON string representation of the object
print(TaskOutletAssetReference.to_json())

# convert the object into a dict
task_outlet_asset_reference_dict = task_outlet_asset_reference_instance.to_dict()
# create an instance of TaskOutletAssetReference from a dict
task_outlet_asset_reference_from_dict = TaskOutletAssetReference.from_dict(task_outlet_asset_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


