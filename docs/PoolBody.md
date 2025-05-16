# PoolBody

Pool serializer for post bodies.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**include_deferred** | **bool** |  | [optional] [default to False]
**name** | **str** |  | 
**slots** | **int** |  | 

## Example

```python
from airflow_client.client.models.pool_body import PoolBody

# TODO update the JSON string below
json = "{}"
# create an instance of PoolBody from a JSON string
pool_body_instance = PoolBody.from_json(json)
# print the JSON string representation of the object
print(PoolBody.to_json())

# convert the object into a dict
pool_body_dict = pool_body_instance.to_dict()
# create an instance of PoolBody from a dict
pool_body_from_dict = PoolBody.from_dict(pool_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


