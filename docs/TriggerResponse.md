# TriggerResponse

Trigger serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classpath** | **str** |  | 
**created_date** | **datetime** |  | 
**id** | **int** |  | 
**kwargs** | **str** |  | 
**triggerer_id** | **int** |  | [optional] 

## Example

```python
from airflow_client.client.models.trigger_response import TriggerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerResponse from a JSON string
trigger_response_instance = TriggerResponse.from_json(json)
# print the JSON string representation of the object
print(TriggerResponse.to_json())

# convert the object into a dict
trigger_response_dict = trigger_response_instance.to_dict()
# create an instance of TriggerResponse from a dict
trigger_response_from_dict = TriggerResponse.from_dict(trigger_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


