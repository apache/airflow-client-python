# BulkCreateActionBulkTaskInstanceBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action to be performed on the entities. | 
**action_on_existence** | [**BulkActionOnExistence**](BulkActionOnExistence.md) |  | [optional] 
**entities** | [**List[BulkTaskInstanceBody]**](BulkTaskInstanceBody.md) | A list of entities to be created. | 

## Example

```python
from airflow_client.client.models.bulk_create_action_bulk_task_instance_body import BulkCreateActionBulkTaskInstanceBody

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCreateActionBulkTaskInstanceBody from a JSON string
bulk_create_action_bulk_task_instance_body_instance = BulkCreateActionBulkTaskInstanceBody.from_json(json)
# print the JSON string representation of the object
print(BulkCreateActionBulkTaskInstanceBody.to_json())

# convert the object into a dict
bulk_create_action_bulk_task_instance_body_dict = bulk_create_action_bulk_task_instance_body_instance.to_dict()
# create an instance of BulkCreateActionBulkTaskInstanceBody from a dict
bulk_create_action_bulk_task_instance_body_from_dict = BulkCreateActionBulkTaskInstanceBody.from_dict(bulk_create_action_bulk_task_instance_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


