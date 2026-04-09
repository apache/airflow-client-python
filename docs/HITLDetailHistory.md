# HITLDetailHistory

Schema for Human-in-the-loop detail history.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_users** | [**List[HITLUser]**](HITLUser.md) |  | [optional] 
**body** | **str** |  | [optional] 
**chosen_options** | **List[str]** |  | [optional] 
**created_at** | **datetime** |  | 
**defaults** | **List[str]** |  | [optional] 
**multiple** | **bool** |  | [optional] [default to False]
**options** | **List[str]** |  | 
**params** | **Dict[str, object]** |  | [optional] 
**params_input** | **Dict[str, object]** |  | [optional] 
**responded_at** | **datetime** |  | [optional] 
**responded_by_user** | [**HITLUser**](HITLUser.md) |  | [optional] 
**response_received** | **bool** |  | [optional] [default to False]
**subject** | **str** |  | 
**task_instance** | [**TaskInstanceHistoryResponse**](TaskInstanceHistoryResponse.md) |  | 

## Example

```python
from airflow_client.client.models.hitl_detail_history import HITLDetailHistory

# TODO update the JSON string below
json = "{}"
# create an instance of HITLDetailHistory from a JSON string
hitl_detail_history_instance = HITLDetailHistory.from_json(json)
# print the JSON string representation of the object
print(HITLDetailHistory.to_json())

# convert the object into a dict
hitl_detail_history_dict = hitl_detail_history_instance.to_dict()
# create an instance of HITLDetailHistory from a dict
hitl_detail_history_from_dict = HITLDetailHistory.from_dict(hitl_detail_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


