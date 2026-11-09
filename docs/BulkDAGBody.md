# BulkDAGBody

Request body for bulk update of Dags.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_id** | **str** |  | 
**is_paused** | **bool** |  | [optional] 
**scheduling_state** | [**DagSchedulingState**](DagSchedulingState.md) |  | [optional] 

## Example

```python
from airflow_client.client.models.bulk_dag_body import BulkDAGBody

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDAGBody from a JSON string
bulk_dag_body_instance = BulkDAGBody.from_json(json)
# print the JSON string representation of the object
print(BulkDAGBody.to_json())

# convert the object into a dict
bulk_dag_body_dict = bulk_dag_body_instance.to_dict()
# create an instance of BulkDAGBody from a dict
bulk_dag_body_from_dict = BulkDAGBody.from_dict(bulk_dag_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


