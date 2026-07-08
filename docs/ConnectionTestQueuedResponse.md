# ConnectionTestQueuedResponse

Response returned when a connection test has been enqueued for worker execution.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **str** |  | 
**state** | **str** |  | 
**token** | **str** |  | 

## Example

```python
from airflow_client.client.models.connection_test_queued_response import ConnectionTestQueuedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionTestQueuedResponse from a JSON string
connection_test_queued_response_instance = ConnectionTestQueuedResponse.from_json(json)
# print the JSON string representation of the object
print(ConnectionTestQueuedResponse.to_json())

# convert the object into a dict
connection_test_queued_response_dict = connection_test_queued_response_instance.to_dict()
# create an instance of ConnectionTestQueuedResponse from a dict
connection_test_queued_response_from_dict = ConnectionTestQueuedResponse.from_dict(connection_test_queued_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


