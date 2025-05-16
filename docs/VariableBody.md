# VariableBody

Variable serializer for bodies.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**key** | **str** |  | 
**value** | **object** |  | 

## Example

```python
from airflow_client.client.models.variable_body import VariableBody

# TODO update the JSON string below
json = "{}"
# create an instance of VariableBody from a JSON string
variable_body_instance = VariableBody.from_json(json)
# print the JSON string representation of the object
print(VariableBody.to_json())

# convert the object into a dict
variable_body_dict = variable_body_instance.to_dict()
# create an instance of VariableBody from a dict
variable_body_from_dict = VariableBody.from_dict(variable_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


