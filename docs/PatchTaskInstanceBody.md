# PatchTaskInstanceBody

Request body for Clear Task Instances endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_downstream** | **bool** |  | [optional] [default to False]
**include_future** | **bool** |  | [optional] [default to False]
**include_past** | **bool** |  | [optional] [default to False]
**include_upstream** | **bool** |  | [optional] [default to False]
**new_state** | [**TaskInstanceState**](TaskInstanceState.md) |  | [optional] 
**note** | **str** |  | [optional] 

## Example

```python
from airflow_client.client.models.patch_task_instance_body import PatchTaskInstanceBody

# TODO update the JSON string below
json = "{}"
# create an instance of PatchTaskInstanceBody from a JSON string
patch_task_instance_body_instance = PatchTaskInstanceBody.from_json(json)
# print the JSON string representation of the object
print(PatchTaskInstanceBody.to_json())

# convert the object into a dict
patch_task_instance_body_dict = patch_task_instance_body_instance.to_dict()
# create an instance of PatchTaskInstanceBody from a dict
patch_task_instance_body_from_dict = PatchTaskInstanceBody.from_dict(patch_task_instance_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


