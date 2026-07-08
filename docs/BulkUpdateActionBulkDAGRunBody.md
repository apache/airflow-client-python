# BulkUpdateActionBulkDAGRunBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action to be performed on the entities. | 
**action_on_non_existence** | [**BulkActionNotOnExistence**](BulkActionNotOnExistence.md) |  | [optional] 
**entities** | [**List[BulkDAGRunBody]**](BulkDAGRunBody.md) | A list of entities to be updated. | 
**update_mask** | **List[str]** |  | [optional] 

## Example

```python
from airflow_client.client.models.bulk_update_action_bulk_dag_run_body import BulkUpdateActionBulkDAGRunBody

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpdateActionBulkDAGRunBody from a JSON string
bulk_update_action_bulk_dag_run_body_instance = BulkUpdateActionBulkDAGRunBody.from_json(json)
# print the JSON string representation of the object
print(BulkUpdateActionBulkDAGRunBody.to_json())

# convert the object into a dict
bulk_update_action_bulk_dag_run_body_dict = bulk_update_action_bulk_dag_run_body_instance.to_dict()
# create an instance of BulkUpdateActionBulkDAGRunBody from a dict
bulk_update_action_bulk_dag_run_body_from_dict = BulkUpdateActionBulkDAGRunBody.from_dict(bulk_update_action_bulk_dag_run_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


