# BulkCreateActionConnectionBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**BulkAction**](BulkAction.md) | The action to be performed on the entities. | 
**action_on_existence** | [**BulkActionOnExistence**](BulkActionOnExistence.md) |  | [optional] 
**entities** | [**List[ConnectionBody]**](ConnectionBody.md) | A list of entities to be created. | 

## Example

```python
from airflow_client.client.models.bulk_create_action_connection_body import BulkCreateActionConnectionBody

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCreateActionConnectionBody from a JSON string
bulk_create_action_connection_body_instance = BulkCreateActionConnectionBody.from_json(json)
# print the JSON string representation of the object
print(BulkCreateActionConnectionBody.to_json())

# convert the object into a dict
bulk_create_action_connection_body_dict = bulk_create_action_connection_body_instance.to_dict()
# create an instance of BulkCreateActionConnectionBody from a dict
bulk_create_action_connection_body_from_dict = BulkCreateActionConnectionBody.from_dict(bulk_create_action_connection_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


