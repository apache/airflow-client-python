# TaskInstancesLogResponse

Log serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**Content**](Content.md) |  | 
**continuation_token** | **str** |  | [optional] 

## Example

```python
from airflow_client.client.models.task_instances_log_response import TaskInstancesLogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TaskInstancesLogResponse from a JSON string
task_instances_log_response_instance = TaskInstancesLogResponse.from_json(json)
# print the JSON string representation of the object
print(TaskInstancesLogResponse.to_json())

# convert the object into a dict
task_instances_log_response_dict = task_instances_log_response_instance.to_dict()
# create an instance of TaskInstancesLogResponse from a dict
task_instances_log_response_from_dict = TaskInstancesLogResponse.from_dict(task_instances_log_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


