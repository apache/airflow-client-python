# TaskDependencyCollectionResponse

Task scheduling dependencies collection serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dependencies** | [**List[TaskDependencyResponse]**](TaskDependencyResponse.md) |  | 

## Example

```python
from airflow_client.client.models.task_dependency_collection_response import TaskDependencyCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TaskDependencyCollectionResponse from a JSON string
task_dependency_collection_response_instance = TaskDependencyCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(TaskDependencyCollectionResponse.to_json())

# convert the object into a dict
task_dependency_collection_response_dict = task_dependency_collection_response_instance.to_dict()
# create an instance of TaskDependencyCollectionResponse from a dict
task_dependency_collection_response_from_dict = TaskDependencyCollectionResponse.from_dict(task_dependency_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


