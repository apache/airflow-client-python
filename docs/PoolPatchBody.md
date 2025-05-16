# PoolPatchBody

Pool serializer for patch bodies.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**include_deferred** | **bool** |  | [optional] 
**pool** | **str** |  | [optional] 
**slots** | **int** |  | [optional] 

## Example

```python
from airflow_client.client.models.pool_patch_body import PoolPatchBody

# TODO update the JSON string below
json = "{}"
# create an instance of PoolPatchBody from a JSON string
pool_patch_body_instance = PoolPatchBody.from_json(json)
# print the JSON string representation of the object
print(PoolPatchBody.to_json())

# convert the object into a dict
pool_patch_body_dict = pool_patch_body_instance.to_dict()
# create an instance of PoolPatchBody from a dict
pool_patch_body_from_dict = PoolPatchBody.from_dict(pool_patch_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


