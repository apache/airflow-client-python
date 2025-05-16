# TaskInstanceCollectionResponse

Task Instance Collection serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_instances** | [**List[TaskInstanceResponse]**](TaskInstanceResponse.md) |  | 
**total_entries** | **int** |  | 

## Example

```python
from airflow_client.client.models.task_instance_collection_response import TaskInstanceCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TaskInstanceCollectionResponse from a JSON string
task_instance_collection_response_instance = TaskInstanceCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(TaskInstanceCollectionResponse.to_json())

# convert the object into a dict
task_instance_collection_response_dict = task_instance_collection_response_instance.to_dict()
# create an instance of TaskInstanceCollectionResponse from a dict
task_instance_collection_response_from_dict = TaskInstanceCollectionResponse.from_dict(task_instance_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


