# SchedulerInstanceInfoResponse

Scheduler instance info serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** |  | [optional] 
**latest_scheduler_heartbeat** | **str** |  | [optional] 

## Example

```python
from airflow_client.client.models.scheduler_instance_info_response import SchedulerInstanceInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulerInstanceInfoResponse from a JSON string
scheduler_instance_info_response_instance = SchedulerInstanceInfoResponse.from_json(json)
# print the JSON string representation of the object
print(SchedulerInstanceInfoResponse.to_json())

# convert the object into a dict
scheduler_instance_info_response_dict = scheduler_instance_info_response_instance.to_dict()
# create an instance of SchedulerInstanceInfoResponse from a dict
scheduler_instance_info_response_from_dict = SchedulerInstanceInfoResponse.from_dict(scheduler_instance_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


