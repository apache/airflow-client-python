# BulkBodyPoolBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[BulkBodyPoolBodyActionsInner]**](BulkBodyPoolBodyActionsInner.md) |  | 

## Example

```python
from airflow_client.client.models.bulk_body_pool_body import BulkBodyPoolBody

# TODO update the JSON string below
json = "{}"
# create an instance of BulkBodyPoolBody from a JSON string
bulk_body_pool_body_instance = BulkBodyPoolBody.from_json(json)
# print the JSON string representation of the object
print(BulkBodyPoolBody.to_json())

# convert the object into a dict
bulk_body_pool_body_dict = bulk_body_pool_body_instance.to_dict()
# create an instance of BulkBodyPoolBody from a dict
bulk_body_pool_body_from_dict = BulkBodyPoolBody.from_dict(bulk_body_pool_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


