# BulkResponse

Serializer for responses to bulk entity operations.  This represents the results of create, update, and delete actions performed on entity in bulk. Each action (if requested) is represented as a field containing details about successful keys and any encountered errors. Fields are populated in the response only if the respective action was part of the request, else are set None.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create** | [**BulkActionResponse**](BulkActionResponse.md) |  | [optional] 
**delete** | [**BulkActionResponse**](BulkActionResponse.md) |  | [optional] 
**update** | [**BulkActionResponse**](BulkActionResponse.md) |  | [optional] 

## Example

```python
from airflow_client.client.models.bulk_response import BulkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkResponse from a JSON string
bulk_response_instance = BulkResponse.from_json(json)
# print the JSON string representation of the object
print(BulkResponse.to_json())

# convert the object into a dict
bulk_response_dict = bulk_response_instance.to_dict()
# create an instance of BulkResponse from a dict
bulk_response_from_dict = BulkResponse.from_dict(bulk_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


