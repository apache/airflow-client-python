# BulkBodyVariableBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[BulkBodyVariableBodyActionsInner]**](BulkBodyVariableBodyActionsInner.md) |  | 

## Example

```python
from airflow_client.client.models.bulk_body_variable_body import BulkBodyVariableBody

# TODO update the JSON string below
json = "{}"
# create an instance of BulkBodyVariableBody from a JSON string
bulk_body_variable_body_instance = BulkBodyVariableBody.from_json(json)
# print the JSON string representation of the object
print(BulkBodyVariableBody.to_json())

# convert the object into a dict
bulk_body_variable_body_dict = bulk_body_variable_body_instance.to_dict()
# create an instance of BulkBodyVariableBody from a dict
bulk_body_variable_body_from_dict = BulkBodyVariableBody.from_dict(bulk_body_variable_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


