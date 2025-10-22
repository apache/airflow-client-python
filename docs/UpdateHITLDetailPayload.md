# UpdateHITLDetailPayload

Schema for updating the content of a Human-in-the-loop detail.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chosen_options** | **List[str]** |  | 
**params_input** | **object** |  | [optional] 

## Example

```python
from airflow_client.client.models.update_hitl_detail_payload import UpdateHITLDetailPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateHITLDetailPayload from a JSON string
update_hitl_detail_payload_instance = UpdateHITLDetailPayload.from_json(json)
# print the JSON string representation of the object
print(UpdateHITLDetailPayload.to_json())

# convert the object into a dict
update_hitl_detail_payload_dict = update_hitl_detail_payload_instance.to_dict()
# create an instance of UpdateHITLDetailPayload from a dict
update_hitl_detail_payload_from_dict = UpdateHITLDetailPayload.from_dict(update_hitl_detail_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


