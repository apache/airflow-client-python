# PoolCollectionResponse

Pool Collection serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pools** | [**List[PoolResponse]**](PoolResponse.md) |  | 
**total_entries** | **int** |  | 

## Example

```python
from airflow_client.client.models.pool_collection_response import PoolCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PoolCollectionResponse from a JSON string
pool_collection_response_instance = PoolCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(PoolCollectionResponse.to_json())

# convert the object into a dict
pool_collection_response_dict = pool_collection_response_instance.to_dict()
# create an instance of PoolCollectionResponse from a dict
pool_collection_response_from_dict = PoolCollectionResponse.from_dict(pool_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


