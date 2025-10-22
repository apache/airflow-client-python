# HITLDetailResponse

Response of updating a Human-in-the-loop detail.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chosen_options** | **List[str]** |  | 
**params_input** | **object** |  | [optional] 
**responded_at** | **datetime** |  | 
**responded_by** | [**HITLUser**](HITLUser.md) |  | 

## Example

```python
from airflow_client.client.models.hitl_detail_response import HITLDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HITLDetailResponse from a JSON string
hitl_detail_response_instance = HITLDetailResponse.from_json(json)
# print the JSON string representation of the object
print(HITLDetailResponse.to_json())

# convert the object into a dict
hitl_detail_response_dict = hitl_detail_response_instance.to_dict()
# create an instance of HITLDetailResponse from a dict
hitl_detail_response_from_dict = HITLDetailResponse.from_dict(hitl_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


