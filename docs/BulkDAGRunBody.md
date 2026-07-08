# BulkDAGRunBody

Request body for bulk operations on Dag Runs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_id** | **str** |  | [optional] 
**dag_run_id** | **str** |  | 
**note** | **str** |  | [optional] 
**state** | [**DagRunMutableStates**](DagRunMutableStates.md) |  | [optional] 

## Example

```python
from airflow_client.client.models.bulk_dag_run_body import BulkDAGRunBody

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDAGRunBody from a JSON string
bulk_dag_run_body_instance = BulkDAGRunBody.from_json(json)
# print the JSON string representation of the object
print(BulkDAGRunBody.to_json())

# convert the object into a dict
bulk_dag_run_body_dict = bulk_dag_run_body_instance.to_dict()
# create an instance of BulkDAGRunBody from a dict
bulk_dag_run_body_from_dict = BulkDAGRunBody.from_dict(bulk_dag_run_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


