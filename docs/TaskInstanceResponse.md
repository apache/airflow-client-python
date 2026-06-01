# TaskInstanceResponse

TaskInstance serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**task_id** | **str** |  | 
**dag_id** | **str** |  | 
**dag_run_id** | **str** |  | 
**map_index** | **int** |  | 
**logical_date** | **datetime** |  | 
**run_after** | **datetime** |  | 
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
**note** | **str** |  | 
**rendered_map_index** | **str** |  | 
**rendered_fields** | **Dict[str, object]** |  | [optional] 
**trigger** | [**TriggerResponse**](TriggerResponse.md) |  | 
**triggerer_job** | [**JobResponse**](JobResponse.md) |  | 
**dag_version** | [**DagVersionResponse**](DagVersionResponse.md) |  | 

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


