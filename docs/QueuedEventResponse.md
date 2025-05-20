# QueuedEventResponse

Queued Event serializer for responses..

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **int** |  | 
**created_at** | **datetime** |  | 
**dag_id** | **str** |  | 

## Example

```python
from airflow_client.client.models.queued_event_response import QueuedEventResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QueuedEventResponse from a JSON string
queued_event_response_instance = QueuedEventResponse.from_json(json)
# print the JSON string representation of the object
print(QueuedEventResponse.to_json())

# convert the object into a dict
queued_event_response_dict = queued_event_response_instance.to_dict()
# create an instance of QueuedEventResponse from a dict
queued_event_response_from_dict = QueuedEventResponse.from_dict(queued_event_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


