# VariableResponse

Variable serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**is_encrypted** | **bool** |  | 
**key** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from airflow_client.client.models.variable_response import VariableResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VariableResponse from a JSON string
variable_response_instance = VariableResponse.from_json(json)
# print the JSON string representation of the object
print(VariableResponse.to_json())

# convert the object into a dict
variable_response_dict = variable_response_instance.to_dict()
# create an instance of VariableResponse from a dict
variable_response_from_dict = VariableResponse.from_dict(variable_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


