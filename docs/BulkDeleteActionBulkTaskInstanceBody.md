# BulkDeleteActionBulkTaskInstanceBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action to be performed on the entities. | 
**action_on_non_existence** | [**BulkActionNotOnExistence**](BulkActionNotOnExistence.md) |  | [optional] 
**entities** | [**List[BulkDeleteActionBulkTaskInstanceBodyEntitiesInner]**](BulkDeleteActionBulkTaskInstanceBodyEntitiesInner.md) | A list of entity id/key or entity objects to be deleted. | 

## Example

```python
from airflow_client.client.models.bulk_delete_action_bulk_task_instance_body import BulkDeleteActionBulkTaskInstanceBody

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDeleteActionBulkTaskInstanceBody from a JSON string
bulk_delete_action_bulk_task_instance_body_instance = BulkDeleteActionBulkTaskInstanceBody.from_json(json)
# print the JSON string representation of the object
print(BulkDeleteActionBulkTaskInstanceBody.to_json())

# convert the object into a dict
bulk_delete_action_bulk_task_instance_body_dict = bulk_delete_action_bulk_task_instance_body_instance.to_dict()
# create an instance of BulkDeleteActionBulkTaskInstanceBody from a dict
bulk_delete_action_bulk_task_instance_body_from_dict = BulkDeleteActionBulkTaskInstanceBody.from_dict(bulk_delete_action_bulk_task_instance_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


