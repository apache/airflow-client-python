# TriggererInstanceInfoResponse

Triggerer instance info serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** |  | [optional] 
**latest_triggerer_heartbeat** | **str** |  | [optional] 
**team_names** | **List[str]** |  | 

## Example

```python
from airflow_client.client.models.triggerer_instance_info_response import TriggererInstanceInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TriggererInstanceInfoResponse from a JSON string
triggerer_instance_info_response_instance = TriggererInstanceInfoResponse.from_json(json)
# print the JSON string representation of the object
print(TriggererInstanceInfoResponse.to_json())

# convert the object into a dict
triggerer_instance_info_response_dict = triggerer_instance_info_response_instance.to_dict()
# create an instance of TriggererInstanceInfoResponse from a dict
triggerer_instance_info_response_from_dict = TriggererInstanceInfoResponse.from_dict(triggerer_instance_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


