# BulkActionResponse

Serializer for individual bulk action responses.  Represents the outcome of a single bulk operation (create, update, or delete). The response includes a list of successful keys and any errors encountered during the operation. This structure helps users understand which key actions succeeded and which failed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **List[object]** | A list of errors encountered during the operation, each containing details about the issue. | [optional] [default to []]
**success** | **List[str]** | A list of unique id/key representing successful operations. | [optional] [default to []]

## Example

```python
from airflow_client.client.models.bulk_action_response import BulkActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkActionResponse from a JSON string
bulk_action_response_instance = BulkActionResponse.from_json(json)
# print the JSON string representation of the object
print(BulkActionResponse.to_json())

# convert the object into a dict
bulk_action_response_dict = bulk_action_response_instance.to_dict()
# create an instance of BulkActionResponse from a dict
bulk_action_response_from_dict = BulkActionResponse.from_dict(bulk_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


