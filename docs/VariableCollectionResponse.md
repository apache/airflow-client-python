# VariableCollectionResponse

Variable Collection serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_entries** | **int** |  | 
**variables** | [**List[VariableResponse]**](VariableResponse.md) |  | 

## Example

```python
from airflow_client.client.models.variable_collection_response import VariableCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VariableCollectionResponse from a JSON string
variable_collection_response_instance = VariableCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(VariableCollectionResponse.to_json())

# convert the object into a dict
variable_collection_response_dict = variable_collection_response_instance.to_dict()
# create an instance of VariableCollectionResponse from a dict
variable_collection_response_from_dict = VariableCollectionResponse.from_dict(variable_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


