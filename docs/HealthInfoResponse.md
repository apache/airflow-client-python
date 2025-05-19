# HealthInfoResponse

Health serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_processor** | [**DagProcessorInfoResponse**](DagProcessorInfoResponse.md) |  | [optional] 
**metadatabase** | [**BaseInfoResponse**](BaseInfoResponse.md) |  | 
**scheduler** | [**SchedulerInfoResponse**](SchedulerInfoResponse.md) |  | 
**triggerer** | [**TriggererInfoResponse**](TriggererInfoResponse.md) |  | 

## Example

```python
from airflow_client.client.models.health_info_response import HealthInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HealthInfoResponse from a JSON string
health_info_response_instance = HealthInfoResponse.from_json(json)
# print the JSON string representation of the object
print(HealthInfoResponse.to_json())

# convert the object into a dict
health_info_response_dict = health_info_response_instance.to_dict()
# create an instance of HealthInfoResponse from a dict
health_info_response_from_dict = HealthInfoResponse.from_dict(health_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


