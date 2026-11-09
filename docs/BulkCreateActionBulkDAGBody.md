# BulkCreateActionBulkDAGBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action to be performed on the entities. | 
**action_on_existence** | [**BulkActionOnExistence**](BulkActionOnExistence.md) |  | [optional] 
**entities** | [**List[BulkDAGBody]**](BulkDAGBody.md) | A list of entities to be created. | 

## Example

```python
from airflow_client.client.models.bulk_create_action_bulk_dag_body import BulkCreateActionBulkDAGBody

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCreateActionBulkDAGBody from a JSON string
bulk_create_action_bulk_dag_body_instance = BulkCreateActionBulkDAGBody.from_json(json)
# print the JSON string representation of the object
print(BulkCreateActionBulkDAGBody.to_json())

# convert the object into a dict
bulk_create_action_bulk_dag_body_dict = bulk_create_action_bulk_dag_body_instance.to_dict()
# create an instance of BulkCreateActionBulkDAGBody from a dict
bulk_create_action_bulk_dag_body_from_dict = BulkCreateActionBulkDAGBody.from_dict(bulk_create_action_bulk_dag_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


