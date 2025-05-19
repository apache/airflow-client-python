# PoolResponse

Pool serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deferred_slots** | **int** |  | 
**description** | **str** |  | [optional] 
**include_deferred** | **bool** |  | 
**name** | **str** |  | 
**occupied_slots** | **int** |  | 
**open_slots** | **int** |  | 
**queued_slots** | **int** |  | 
**running_slots** | **int** |  | 
**scheduled_slots** | **int** |  | 
**slots** | **int** |  | 

## Example

```python
from airflow_client.client.models.pool_response import PoolResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PoolResponse from a JSON string
pool_response_instance = PoolResponse.from_json(json)
# print the JSON string representation of the object
print(PoolResponse.to_json())

# convert the object into a dict
pool_response_dict = pool_response_instance.to_dict()
# create an instance of PoolResponse from a dict
pool_response_from_dict = PoolResponse.from_dict(pool_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


