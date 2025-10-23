# HITLUser

Schema for a Human-in-the-loop users.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from airflow_client.client.models.hitl_user import HITLUser

# TODO update the JSON string below
json = "{}"
# create an instance of HITLUser from a JSON string
hitl_user_instance = HITLUser.from_json(json)
# print the JSON string representation of the object
print(HITLUser.to_json())

# convert the object into a dict
hitl_user_dict = hitl_user_instance.to_dict()
# create an instance of HITLUser from a dict
hitl_user_from_dict = HITLUser.from_dict(hitl_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


