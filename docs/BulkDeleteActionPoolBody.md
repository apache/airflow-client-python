# BulkDeleteActionPoolBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**BulkAction**](BulkAction.md) | The action to be performed on the entities. | 
**action_on_non_existence** | [**BulkActionNotOnExistence**](BulkActionNotOnExistence.md) |  | [optional] 
**entities** | **List[str]** | A list of entity id/key to be deleted. | 

## Example

```python
from airflow_client.client.models.bulk_delete_action_pool_body import BulkDeleteActionPoolBody

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDeleteActionPoolBody from a JSON string
bulk_delete_action_pool_body_instance = BulkDeleteActionPoolBody.from_json(json)
# print the JSON string representation of the object
print(BulkDeleteActionPoolBody.to_json())

# convert the object into a dict
bulk_delete_action_pool_body_dict = bulk_delete_action_pool_body_instance.to_dict()
# create an instance of BulkDeleteActionPoolBody from a dict
bulk_delete_action_pool_body_from_dict = BulkDeleteActionPoolBody.from_dict(bulk_delete_action_pool_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


