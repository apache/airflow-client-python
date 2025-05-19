# ConnectionTestResponse

Connection Test serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**status** | **bool** |  | 

## Example

```python
from airflow_client.client.models.connection_test_response import ConnectionTestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionTestResponse from a JSON string
connection_test_response_instance = ConnectionTestResponse.from_json(json)
# print the JSON string representation of the object
print(ConnectionTestResponse.to_json())

# convert the object into a dict
connection_test_response_dict = connection_test_response_instance.to_dict()
# create an instance of ConnectionTestResponse from a dict
connection_test_response_from_dict = ConnectionTestResponse.from_dict(connection_test_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


