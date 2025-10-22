# BulkTaskInstanceBody

Request body for bulk update, and delete task instances.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_downstream** | **bool** |  | [optional] [default to False]
**include_future** | **bool** |  | [optional] [default to False]
**include_past** | **bool** |  | [optional] [default to False]
**include_upstream** | **bool** |  | [optional] [default to False]
**map_index** | **int** |  | [optional] 
**new_state** | [**TaskInstanceState**](TaskInstanceState.md) |  | [optional] 
**note** | **str** |  | [optional] 
**task_id** | **str** |  | 

## Example

```python
from airflow_client.client.models.bulk_task_instance_body import BulkTaskInstanceBody

# TODO update the JSON string below
json = "{}"
# create an instance of BulkTaskInstanceBody from a JSON string
bulk_task_instance_body_instance = BulkTaskInstanceBody.from_json(json)
# print the JSON string representation of the object
print(BulkTaskInstanceBody.to_json())

# convert the object into a dict
bulk_task_instance_body_dict = bulk_task_instance_body_instance.to_dict()
# create an instance of BulkTaskInstanceBody from a dict
bulk_task_instance_body_from_dict = BulkTaskInstanceBody.from_dict(bulk_task_instance_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


