# TaskDependencyResponse

Task Dependency serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**reason** | **str** |  | 

## Example

```python
from airflow_client.client.models.task_dependency_response import TaskDependencyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TaskDependencyResponse from a JSON string
task_dependency_response_instance = TaskDependencyResponse.from_json(json)
# print the JSON string representation of the object
print(TaskDependencyResponse.to_json())

# convert the object into a dict
task_dependency_response_dict = task_dependency_response_instance.to_dict()
# create an instance of TaskDependencyResponse from a dict
task_dependency_response_from_dict = TaskDependencyResponse.from_dict(task_dependency_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


