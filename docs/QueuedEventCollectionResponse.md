# QueuedEventCollectionResponse

Queued Event Collection serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queued_events** | [**List[QueuedEventResponse]**](QueuedEventResponse.md) |  | 
**total_entries** | **int** |  | 

## Example

```python
from airflow_client.client.models.queued_event_collection_response import QueuedEventCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QueuedEventCollectionResponse from a JSON string
queued_event_collection_response_instance = QueuedEventCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(QueuedEventCollectionResponse.to_json())

# convert the object into a dict
queued_event_collection_response_dict = queued_event_collection_response_instance.to_dict()
# create an instance of QueuedEventCollectionResponse from a dict
queued_event_collection_response_from_dict = QueuedEventCollectionResponse.from_dict(queued_event_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


