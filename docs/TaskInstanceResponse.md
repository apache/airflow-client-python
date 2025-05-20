# TaskInstanceResponse

TaskInstance serializer for responses.

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
**id** | **str** |  | 
**logical_date** | **datetime** |  | [optional] 
**map_index** | **int** |  | 
**max_tries** | **int** |  | 
**note** | **str** |  | [optional] 
**operator** | **str** |  | [optional] 
**pid** | **int** |  | [optional] 
**pool** | **str** |  | 
**pool_slots** | **int** |  | 
**priority_weight** | **int** |  | [optional] 
**queue** | **str** |  | [optional] 
**queued_when** | **datetime** |  | [optional] 
**rendered_fields** | **object** |  | [optional] 
**rendered_map_index** | **str** |  | [optional] 
**run_after** | **datetime** |  | 
**scheduled_when** | **datetime** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**state** | [**TaskInstanceState**](TaskInstanceState.md) |  | [optional] 
**task_display_name** | **str** |  | 
**task_id** | **str** |  | 
**trigger** | [**TriggerResponse**](TriggerResponse.md) |  | [optional] 
**triggerer_job** | [**JobResponse**](JobResponse.md) |  | [optional] 
**try_number** | **int** |  | 
**unixname** | **str** |  | [optional] 

## Example

```python
from airflow_client.client.models.task_instance_response import TaskInstanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TaskInstanceResponse from a JSON string
task_instance_response_instance = TaskInstanceResponse.from_json(json)
# print the JSON string representation of the object
print(TaskInstanceResponse.to_json())

# convert the object into a dict
task_instance_response_dict = task_instance_response_instance.to_dict()
# create an instance of TaskInstanceResponse from a dict
task_instance_response_from_dict = TaskInstanceResponse.from_dict(task_instance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


