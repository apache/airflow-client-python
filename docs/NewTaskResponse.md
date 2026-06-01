# NewTaskResponse

Lightweight response for new tasks that don't have TaskInstances yet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_display_name** | **str** |  | 
**task_id** | **str** |  | 

## Example

```python
from airflow_client.client.models.new_task_response import NewTaskResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NewTaskResponse from a JSON string
new_task_response_instance = NewTaskResponse.from_json(json)
# print the JSON string representation of the object
print(NewTaskResponse.to_json())

# convert the object into a dict
new_task_response_dict = new_task_response_instance.to_dict()
# create an instance of NewTaskResponse from a dict
new_task_response_from_dict = NewTaskResponse.from_dict(new_task_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


