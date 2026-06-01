# TaskInstanceHistoryResponse

TaskInstanceHistory serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** |  | 
**dag_id** | **str** |  | 
**dag_run_id** | **str** |  | 
**map_index** | **int** |  | 
**start_date** | **datetime** |  | 
**end_date** | **datetime** |  | 
**duration** | **float** |  | 
**state** | [**TaskInstanceState**](TaskInstanceState.md) |  | 
**try_number** | **int** |  | 
**max_tries** | **int** |  | 
**task_display_name** | **str** |  | 
**dag_display_name** | **str** |  | 
**hostname** | **str** |  | 
**unixname** | **str** |  | 
**pool** | **str** |  | 
**pool_slots** | **int** |  | 
**queue** | **str** |  | 
**priority_weight** | **int** |  | 
**operator** | **str** |  | 
**operator_name** | **str** |  | 
**queued_when** | **datetime** |  | 
**scheduled_when** | **datetime** |  | 
**pid** | **int** |  | 
**executor** | **str** |  | 
**executor_config** | **str** |  | 
**dag_version** | [**DagVersionResponse**](DagVersionResponse.md) |  | 

## Example

```python
from airflow_client.client.models.task_instance_history_response import TaskInstanceHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TaskInstanceHistoryResponse from a JSON string
task_instance_history_response_instance = TaskInstanceHistoryResponse.from_json(json)
# print the JSON string representation of the object
print(TaskInstanceHistoryResponse.to_json())

# convert the object into a dict
task_instance_history_response_dict = task_instance_history_response_instance.to_dict()
# create an instance of TaskInstanceHistoryResponse from a dict
task_instance_history_response_from_dict = TaskInstanceHistoryResponse.from_dict(task_instance_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


