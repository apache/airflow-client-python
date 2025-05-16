# SchedulerInfoResponse

Scheduler info serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latest_scheduler_heartbeat** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from airflow_client.client.models.scheduler_info_response import SchedulerInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulerInfoResponse from a JSON string
scheduler_info_response_instance = SchedulerInfoResponse.from_json(json)
# print the JSON string representation of the object
print(SchedulerInfoResponse.to_json())

# convert the object into a dict
scheduler_info_response_dict = scheduler_info_response_instance.to_dict()
# create an instance of SchedulerInfoResponse from a dict
scheduler_info_response_from_dict = SchedulerInfoResponse.from_dict(scheduler_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


