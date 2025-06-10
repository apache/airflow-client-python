# BulkUpdateActionConnectionBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action to be performed on the entities. | 
**action_on_non_existence** | [**BulkActionNotOnExistence**](BulkActionNotOnExistence.md) |  | [optional] 
**entities** | [**List[ConnectionBody]**](ConnectionBody.md) | A list of entities to be updated. | 

## Example

```python
from airflow_client.client.models.bulk_update_action_connection_body import BulkUpdateActionConnectionBody

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpdateActionConnectionBody from a JSON string
bulk_update_action_connection_body_instance = BulkUpdateActionConnectionBody.from_json(json)
# print the JSON string representation of the object
print(BulkUpdateActionConnectionBody.to_json())

# convert the object into a dict
bulk_update_action_connection_body_dict = bulk_update_action_connection_body_instance.to_dict()
# create an instance of BulkUpdateActionConnectionBody from a dict
bulk_update_action_connection_body_from_dict = BulkUpdateActionConnectionBody.from_dict(bulk_update_action_connection_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


