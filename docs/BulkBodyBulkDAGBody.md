# BulkBodyBulkDAGBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[ActionsInner]**](ActionsInner.md) |  | 

## Example

```python
from airflow_client.client.models.bulk_body_bulk_dag_body import BulkBodyBulkDAGBody

# TODO update the JSON string below
json = "{}"
# create an instance of BulkBodyBulkDAGBody from a JSON string
bulk_body_bulk_dag_body_instance = BulkBodyBulkDAGBody.from_json(json)
# print the JSON string representation of the object
print(BulkBodyBulkDAGBody.to_json())

# convert the object into a dict
bulk_body_bulk_dag_body_dict = bulk_body_bulk_dag_body_instance.to_dict()
# create an instance of BulkBodyBulkDAGBody from a dict
bulk_body_bulk_dag_body_from_dict = BulkBodyBulkDAGBody.from_dict(bulk_body_bulk_dag_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


