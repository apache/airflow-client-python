# BulkBodyConnectionBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[BulkBodyConnectionBodyActionsInner]**](BulkBodyConnectionBodyActionsInner.md) |  | 

## Example

```python
from airflow_client.client.models.bulk_body_connection_body import BulkBodyConnectionBody

# TODO update the JSON string below
json = "{}"
# create an instance of BulkBodyConnectionBody from a JSON string
bulk_body_connection_body_instance = BulkBodyConnectionBody.from_json(json)
# print the JSON string representation of the object
print(BulkBodyConnectionBody.to_json())

# convert the object into a dict
bulk_body_connection_body_dict = bulk_body_connection_body_instance.to_dict()
# create an instance of BulkBodyConnectionBody from a dict
bulk_body_connection_body_from_dict = BulkBodyConnectionBody.from_dict(bulk_body_connection_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


