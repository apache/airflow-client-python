# EventLogCollectionResponse

Event Log Collection Response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_logs** | [**List[EventLogResponse]**](EventLogResponse.md) |  | 
**total_entries** | **int** |  | 

## Example

```python
from airflow_client.client.models.event_log_collection_response import EventLogCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EventLogCollectionResponse from a JSON string
event_log_collection_response_instance = EventLogCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(EventLogCollectionResponse.to_json())

# convert the object into a dict
event_log_collection_response_dict = event_log_collection_response_instance.to_dict()
# create an instance of EventLogCollectionResponse from a dict
event_log_collection_response_from_dict = EventLogCollectionResponse.from_dict(event_log_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


