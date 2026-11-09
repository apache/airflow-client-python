# ClearTaskInstancesBody

Request body for Clear Task Instances endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_run_id** | **str** |  | [optional] 
**dry_run** | **bool** |  | [optional] [default to True]
**end_date** | **datetime** |  | [optional] 
**include_downstream** | **bool** |  | [optional] [default to False]
**include_future** | **bool** |  | [optional] [default to False]
**include_later_loop_iterations** | **bool** | Clear later iterations when the selection includes a loop gate. | [optional] [default to True]
**include_past** | **bool** |  | [optional] [default to False]
**include_upstream** | **bool** |  | [optional] [default to False]
**keep_task_state** | **bool** | Keep the task state store entries of the cleared task instances so the next attempt resumes from them. By default they are discarded, so the task starts over. | [optional] [default to False]
**note** | **str** |  | [optional] 
**only_failed** | **bool** |  | [optional] [default to True]
**only_running** | **bool** |  | [optional] [default to False]
**prevent_running_task** | **bool** |  | [optional] [default to False]
**reset_dag_runs** | **bool** |  | [optional] [default to True]
**run_on_latest_version** | **bool** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**task_group_id** | **str** |  | [optional] 
**task_ids** | [**List[ClearTaskInstancesBodyTaskIdsInner]**](ClearTaskInstancesBodyTaskIdsInner.md) |  | [optional] 
**task_instance_ids** | **List[UUID]** |  | [optional] 
**whole_expansion_ids** | **List[UUID]** | Selected execution IDs whose entire mapped expansion should be cleared. | [optional] 

## Example

```python
from airflow_client.client.models.clear_task_instances_body import ClearTaskInstancesBody

# TODO update the JSON string below
json = "{}"
# create an instance of ClearTaskInstancesBody from a JSON string
clear_task_instances_body_instance = ClearTaskInstancesBody.from_json(json)
# print the JSON string representation of the object
print(ClearTaskInstancesBody.to_json())

# convert the object into a dict
clear_task_instances_body_dict = clear_task_instances_body_instance.to_dict()
# create an instance of ClearTaskInstancesBody from a dict
clear_task_instances_body_from_dict = ClearTaskInstancesBody.from_dict(clear_task_instances_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


