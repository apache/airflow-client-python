# AssetCollectionResponse

Asset collection response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**List[AssetResponse]**](AssetResponse.md) |  | 
**total_entries** | **int** |  | 

## Example

```python
from airflow_client.client.models.asset_collection_response import AssetCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssetCollectionResponse from a JSON string
asset_collection_response_instance = AssetCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(AssetCollectionResponse.to_json())

# convert the object into a dict
asset_collection_response_dict = asset_collection_response_instance.to_dict()
# create an instance of AssetCollectionResponse from a dict
asset_collection_response_from_dict = AssetCollectionResponse.from_dict(asset_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


