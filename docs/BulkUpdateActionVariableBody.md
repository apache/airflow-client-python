# BulkUpdateActionVariableBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**BulkAction**](BulkAction.md) | The action to be performed on the entities. | 
**action_on_non_existence** | [**BulkActionNotOnExistence**](BulkActionNotOnExistence.md) |  | [optional] 
**entities** | [**List[VariableBody]**](VariableBody.md) | A list of entities to be updated. | 

## Example

```python
from airflow_client.client.models.bulk_update_action_variable_body import BulkUpdateActionVariableBody

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpdateActionVariableBody from a JSON string
bulk_update_action_variable_body_instance = BulkUpdateActionVariableBody.from_json(json)
# print the JSON string representation of the object
print(BulkUpdateActionVariableBody.to_json())

# convert the object into a dict
bulk_update_action_variable_body_dict = bulk_update_action_variable_body_instance.to_dict()
# create an instance of BulkUpdateActionVariableBody from a dict
bulk_update_action_variable_body_from_dict = BulkUpdateActionVariableBody.from_dict(bulk_update_action_variable_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


