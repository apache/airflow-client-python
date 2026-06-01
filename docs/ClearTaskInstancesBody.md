# ClearTaskInstancesBody

Request body for Clear Task Instances endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **bool** |  | [optional] [default to True]
**start_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**only_failed** | **bool** |  | [optional] [default to True]
**only_running** | **bool** |  | [optional] [default to False]
**reset_dag_runs** | **bool** |  | [optional] [default to True]
**task_ids** | [**List[ClearTaskInstancesBodyTaskIdsInner]**](ClearTaskInstancesBodyTaskIdsInner.md) | A list of &#x60;task_id&#x60; or [&#x60;task_id&#x60;, &#x60;map_index&#x60;]. If only the &#x60;task_id&#x60; is provided for a mapped task, all of its map indices will be targeted. | [optional] 
**dag_run_id** | **str** |  | [optional] 
**include_upstream** | **bool** |  | [optional] [default to False]
**include_downstream** | **bool** |  | [optional] [default to False]
**include_future** | **bool** |  | [optional] [default to False]
**include_past** | **bool** |  | [optional] [default to False]
**run_on_latest_version** | **bool** | (Experimental) Run on the latest bundle version of the dag after clearing the task instances. | [optional] [default to False]
**prevent_running_task** | **bool** |  | [optional] [default to False]

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


