# BulkBodyBulkTaskInstanceBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[BulkBodyBulkTaskInstanceBodyActionsInner]**](BulkBodyBulkTaskInstanceBodyActionsInner.md) |  | 

## Example

```python
from airflow_client.client.models.bulk_body_bulk_task_instance_body import BulkBodyBulkTaskInstanceBody

# TODO update the JSON string below
json = "{}"
# create an instance of BulkBodyBulkTaskInstanceBody from a JSON string
bulk_body_bulk_task_instance_body_instance = BulkBodyBulkTaskInstanceBody.from_json(json)
# print the JSON string representation of the object
print(BulkBodyBulkTaskInstanceBody.to_json())

# convert the object into a dict
bulk_body_bulk_task_instance_body_dict = bulk_body_bulk_task_instance_body_instance.to_dict()
# create an instance of BulkBodyBulkTaskInstanceBody from a dict
bulk_body_bulk_task_instance_body_from_dict = BulkBodyBulkTaskInstanceBody.from_dict(bulk_body_bulk_task_instance_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


