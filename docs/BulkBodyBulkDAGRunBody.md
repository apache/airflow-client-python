# BulkBodyBulkDAGRunBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[ActionsInner]**](ActionsInner.md) |  | 

## Example

```python
from airflow_client.client.models.bulk_body_bulk_dag_run_body import BulkBodyBulkDAGRunBody

# TODO update the JSON string below
json = "{}"
# create an instance of BulkBodyBulkDAGRunBody from a JSON string
bulk_body_bulk_dag_run_body_instance = BulkBodyBulkDAGRunBody.from_json(json)
# print the JSON string representation of the object
print(BulkBodyBulkDAGRunBody.to_json())

# convert the object into a dict
bulk_body_bulk_dag_run_body_dict = bulk_body_bulk_dag_run_body_instance.to_dict()
# create an instance of BulkBodyBulkDAGRunBody from a dict
bulk_body_bulk_dag_run_body_from_dict = BulkBodyBulkDAGRunBody.from_dict(bulk_body_bulk_dag_run_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


