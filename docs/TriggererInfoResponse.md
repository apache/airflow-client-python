# TriggererInfoResponse

Triggerer info serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latest_triggerer_heartbeat** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from airflow_client.client.models.triggerer_info_response import TriggererInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TriggererInfoResponse from a JSON string
triggerer_info_response_instance = TriggererInfoResponse.from_json(json)
# print the JSON string representation of the object
print(TriggererInfoResponse.to_json())

# convert the object into a dict
triggerer_info_response_dict = triggerer_info_response_instance.to_dict()
# create an instance of TriggererInfoResponse from a dict
triggerer_info_response_from_dict = TriggererInfoResponse.from_dict(triggerer_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


