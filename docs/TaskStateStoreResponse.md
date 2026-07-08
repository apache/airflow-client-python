# TaskStateStoreResponse

A single task state store key/value pair with metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **datetime** |  | [optional] 
**key** | **str** |  | 
**updated_at** | **datetime** |  | 
**value** | **object** |  | 

## Example

```python
from airflow_client.client.models.task_state_store_response import TaskStateStoreResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TaskStateStoreResponse from a JSON string
task_state_store_response_instance = TaskStateStoreResponse.from_json(json)
# print the JSON string representation of the object
print(TaskStateStoreResponse.to_json())

# convert the object into a dict
task_state_store_response_dict = task_state_store_response_instance.to_dict()
# create an instance of TaskStateStoreResponse from a dict
task_state_store_response_from_dict = TaskStateStoreResponse.from_dict(task_state_store_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


