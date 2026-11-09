# ActionsInner5


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action to be performed on the entities. | 
**action_on_existence** | [**BulkActionOnExistence**](BulkActionOnExistence.md) |  | [optional] 
**entities** | [**List[EntitiesInner5]**](EntitiesInner5.md) | A list of entity id/key or entity objects to be deleted. | 
**action_on_non_existence** | [**BulkActionNotOnExistence**](BulkActionNotOnExistence.md) |  | [optional] 
**update_mask** | **List[str]** |  | [optional] 

## Example

```python
from airflow_client.client.models.actions_inner5 import ActionsInner5

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsInner5 from a JSON string
actions_inner5_instance = ActionsInner5.from_json(json)
# print the JSON string representation of the object
print(ActionsInner5.to_json())

# convert the object into a dict
actions_inner5_dict = actions_inner5_instance.to_dict()
# create an instance of ActionsInner5 from a dict
actions_inner5_from_dict = ActionsInner5.from_dict(actions_inner5_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


