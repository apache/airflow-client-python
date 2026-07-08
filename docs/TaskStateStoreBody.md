# TaskStateStoreBody

Request body for setting a task state store value.  ``expires_at`` controls expiry:  - ``\"default\"``: apply the configured ``[state_store] default_retention_days``. - ``null``: never expire. - aware datetime: expire at that time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | [**ExpiresAt**](ExpiresAt.md) |  | [optional] 
**value** | **object** |  | 

## Example

```python
from airflow_client.client.models.task_state_store_body import TaskStateStoreBody

# TODO update the JSON string below
json = "{}"
# create an instance of TaskStateStoreBody from a JSON string
task_state_store_body_instance = TaskStateStoreBody.from_json(json)
# print the JSON string representation of the object
print(TaskStateStoreBody.to_json())

# convert the object into a dict
task_state_store_body_dict = task_state_store_body_instance.to_dict()
# create an instance of TaskStateStoreBody from a dict
task_state_store_body_from_dict = TaskStateStoreBody.from_dict(task_state_store_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


