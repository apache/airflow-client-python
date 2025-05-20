# TaskInstanceHistoryResponse

TaskInstanceHistory serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_id** | **str** |  | 
**dag_run_id** | **str** |  | 
**dag_version** | [**DagVersionResponse**](DagVersionResponse.md) |  | [optional] 
**duration** | **float** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**executor** | **str** |  | [optional] 
**executor_config** | **str** |  | 
**hostname** | **str** |  | [optional] 
**map_index** | **int** |  | 
**max_tries** | **int** |  | 
**operator** | **str** |  | [optional] 
**pid** | **int** |  | [optional] 
**pool** | **str** |  | 
**pool_slots** | **int** |  | 
**priority_weight** | **int** |  | [optional] 
**queue** | **str** |  | [optional] 
**queued_when** | **datetime** |  | [optional] 
**scheduled_when** | **datetime** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**state** | [**TaskInstanceState**](TaskInstanceState.md) |  | [optional] 
**task_display_name** | **str** |  | 
**task_id** | **str** |  | 
**try_number** | **int** |  | 
**unixname** | **str** |  | [optional] 

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


