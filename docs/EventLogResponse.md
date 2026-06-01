# EventLogResponse

Event Log Response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_log_id** | **int** |  | 
**when** | **datetime** |  | 
**dag_id** | **str** |  | 
**task_id** | **str** |  | 
**run_id** | **str** |  | 
**map_index** | **int** |  | 
**try_number** | **int** |  | 
**event** | **str** |  | 
**logical_date** | **datetime** |  | 
**owner** | **str** |  | 
**extra** | **str** |  | 
**dag_display_name** | **str** |  | [optional] 
**task_display_name** | **str** |  | [optional] 

## Example

```python
from airflow_client.client.models.event_log_response import EventLogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EventLogResponse from a JSON string
event_log_response_instance = EventLogResponse.from_json(json)
# print the JSON string representation of the object
print(EventLogResponse.to_json())

# convert the object into a dict
event_log_response_dict = event_log_response_instance.to_dict()
# create an instance of EventLogResponse from a dict
event_log_response_from_dict = EventLogResponse.from_dict(event_log_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


