# TaskStateStoreCollectionResponse

All task state store entries for a task instance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_state_store** | [**List[TaskStateStoreResponse]**](TaskStateStoreResponse.md) |  | 
**total_entries** | **int** |  | 

## Example

```python
from airflow_client.client.models.task_state_store_collection_response import TaskStateStoreCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TaskStateStoreCollectionResponse from a JSON string
task_state_store_collection_response_instance = TaskStateStoreCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(TaskStateStoreCollectionResponse.to_json())

# convert the object into a dict
task_state_store_collection_response_dict = task_state_store_collection_response_instance.to_dict()
# create an instance of TaskStateStoreCollectionResponse from a dict
task_state_store_collection_response_from_dict = TaskStateStoreCollectionResponse.from_dict(task_state_store_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


