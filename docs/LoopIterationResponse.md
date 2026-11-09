# LoopIterationResponse

A task execution's position in an enclosing loop.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iteration** | **int** | Position in the enclosing loop, counting from one. | 
**loop_id** | **str** |  | 

## Example

```python
from airflow_client.client.models.loop_iteration_response import LoopIterationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LoopIterationResponse from a JSON string
loop_iteration_response_instance = LoopIterationResponse.from_json(json)
# print the JSON string representation of the object
print(LoopIterationResponse.to_json())

# convert the object into a dict
loop_iteration_response_dict = loop_iteration_response_instance.to_dict()
# create an instance of LoopIterationResponse from a dict
loop_iteration_response_from_dict = LoopIterationResponse.from_dict(loop_iteration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


