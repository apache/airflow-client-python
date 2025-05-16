# TaskInstancesBatchBody

Task Instance body for get batch.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_ids** | **List[str]** |  | [optional] 
**dag_run_ids** | **List[str]** |  | [optional] 
**duration_gte** | **float** |  | [optional] 
**duration_lte** | **float** |  | [optional] 
**end_date_gte** | **datetime** |  | [optional] 
**end_date_lte** | **datetime** |  | [optional] 
**executor** | **List[str]** |  | [optional] 
**logical_date_gte** | **datetime** |  | [optional] 
**logical_date_lte** | **datetime** |  | [optional] 
**order_by** | **str** |  | [optional] 
**page_limit** | **int** |  | [optional] [default to 100]
**page_offset** | **int** |  | [optional] [default to 0]
**pool** | **List[str]** |  | [optional] 
**queue** | **List[str]** |  | [optional] 
**run_after_gte** | **datetime** |  | [optional] 
**run_after_lte** | **datetime** |  | [optional] 
**start_date_gte** | **datetime** |  | [optional] 
**start_date_lte** | **datetime** |  | [optional] 
**state** | [**List[Optional[TaskInstanceState]]**](TaskInstanceState.md) |  | [optional] 
**task_ids** | **List[str]** |  | [optional] 

## Example

```python
from airflow_client.client.models.task_instances_batch_body import TaskInstancesBatchBody

# TODO update the JSON string below
json = "{}"
# create an instance of TaskInstancesBatchBody from a JSON string
task_instances_batch_body_instance = TaskInstancesBatchBody.from_json(json)
# print the JSON string representation of the object
print(TaskInstancesBatchBody.to_json())

# convert the object into a dict
task_instances_batch_body_dict = task_instances_batch_body_instance.to_dict()
# create an instance of TaskInstancesBatchBody from a dict
task_instances_batch_body_from_dict = TaskInstancesBatchBody.from_dict(task_instances_batch_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


