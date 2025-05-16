# DagRunAssetReference

DAGRun serializer for asset responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_id** | **str** |  | 
**data_interval_end** | **datetime** |  | [optional] 
**data_interval_start** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**logical_date** | **datetime** |  | [optional] 
**run_id** | **str** |  | 
**start_date** | **datetime** |  | 
**state** | **str** |  | 

## Example

```python
from airflow_client.client.models.dag_run_asset_reference import DagRunAssetReference

# TODO update the JSON string below
json = "{}"
# create an instance of DagRunAssetReference from a JSON string
dag_run_asset_reference_instance = DagRunAssetReference.from_json(json)
# print the JSON string representation of the object
print(DagRunAssetReference.to_json())

# convert the object into a dict
dag_run_asset_reference_dict = dag_run_asset_reference_instance.to_dict()
# create an instance of DagRunAssetReference from a dict
dag_run_asset_reference_from_dict = DagRunAssetReference.from_dict(dag_run_asset_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


