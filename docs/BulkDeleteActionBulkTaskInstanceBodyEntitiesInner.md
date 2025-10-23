# BulkDeleteActionBulkTaskInstanceBodyEntitiesInner


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
from airflow_client.client.models.bulk_delete_action_bulk_task_instance_body_entities_inner import BulkDeleteActionBulkTaskInstanceBodyEntitiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDeleteActionBulkTaskInstanceBodyEntitiesInner from a JSON string
bulk_delete_action_bulk_task_instance_body_entities_inner_instance = BulkDeleteActionBulkTaskInstanceBodyEntitiesInner.from_json(json)
# print the JSON string representation of the object
print(BulkDeleteActionBulkTaskInstanceBodyEntitiesInner.to_json())

# convert the object into a dict
bulk_delete_action_bulk_task_instance_body_entities_inner_dict = bulk_delete_action_bulk_task_instance_body_entities_inner_instance.to_dict()
# create an instance of BulkDeleteActionBulkTaskInstanceBodyEntitiesInner from a dict
bulk_delete_action_bulk_task_instance_body_entities_inner_from_dict = BulkDeleteActionBulkTaskInstanceBodyEntitiesInner.from_dict(bulk_delete_action_bulk_task_instance_body_entities_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


