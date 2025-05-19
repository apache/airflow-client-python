# DagScheduleAssetReference

DAG schedule reference serializer for assets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**dag_id** | **str** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from airflow_client.client.models.dag_schedule_asset_reference import DagScheduleAssetReference

# TODO update the JSON string below
json = "{}"
# create an instance of DagScheduleAssetReference from a JSON string
dag_schedule_asset_reference_instance = DagScheduleAssetReference.from_json(json)
# print the JSON string representation of the object
print(DagScheduleAssetReference.to_json())

# convert the object into a dict
dag_schedule_asset_reference_dict = dag_schedule_asset_reference_instance.to_dict()
# create an instance of DagScheduleAssetReference from a dict
dag_schedule_asset_reference_from_dict = DagScheduleAssetReference.from_dict(dag_schedule_asset_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


