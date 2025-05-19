# TaskInstanceHistoryCollectionResponse

TaskInstanceHistory Collection serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_instances** | [**List[TaskInstanceHistoryResponse]**](TaskInstanceHistoryResponse.md) |  | 
**total_entries** | **int** |  | 

## Example

```python
from airflow_client.client.models.task_instance_history_collection_response import TaskInstanceHistoryCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TaskInstanceHistoryCollectionResponse from a JSON string
task_instance_history_collection_response_instance = TaskInstanceHistoryCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(TaskInstanceHistoryCollectionResponse.to_json())

# convert the object into a dict
task_instance_history_collection_response_dict = task_instance_history_collection_response_instance.to_dict()
# create an instance of TaskInstanceHistoryCollectionResponse from a dict
task_instance_history_collection_response_from_dict = TaskInstanceHistoryCollectionResponse.from_dict(task_instance_history_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


