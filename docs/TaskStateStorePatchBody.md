# TaskStateStorePatchBody

Request body for patching only the value of an existing task state store key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **object** |  | 

## Example

```python
from airflow_client.client.models.task_state_store_patch_body import TaskStateStorePatchBody

# TODO update the JSON string below
json = "{}"
# create an instance of TaskStateStorePatchBody from a JSON string
task_state_store_patch_body_instance = TaskStateStorePatchBody.from_json(json)
# print the JSON string representation of the object
print(TaskStateStorePatchBody.to_json())

# convert the object into a dict
task_state_store_patch_body_dict = task_state_store_patch_body_instance.to_dict()
# create an instance of TaskStateStorePatchBody from a dict
task_state_store_patch_body_from_dict = TaskStateStorePatchBody.from_dict(task_state_store_patch_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


