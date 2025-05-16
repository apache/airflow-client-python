# BulkBodyConnectionBodyActionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**BulkAction**](BulkAction.md) | The action to be performed on the entities. | 
**action_on_existence** | [**BulkActionOnExistence**](BulkActionOnExistence.md) |  | [optional] 
**entities** | **List[str]** | A list of entity id/key to be deleted. | 
**action_on_non_existence** | [**BulkActionNotOnExistence**](BulkActionNotOnExistence.md) |  | [optional] 

## Example

```python
from airflow_client.client.models.bulk_body_connection_body_actions_inner import BulkBodyConnectionBodyActionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BulkBodyConnectionBodyActionsInner from a JSON string
bulk_body_connection_body_actions_inner_instance = BulkBodyConnectionBodyActionsInner.from_json(json)
# print the JSON string representation of the object
print(BulkBodyConnectionBodyActionsInner.to_json())

# convert the object into a dict
bulk_body_connection_body_actions_inner_dict = bulk_body_connection_body_actions_inner_instance.to_dict()
# create an instance of BulkBodyConnectionBodyActionsInner from a dict
bulk_body_connection_body_actions_inner_from_dict = BulkBodyConnectionBodyActionsInner.from_dict(bulk_body_connection_body_actions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


