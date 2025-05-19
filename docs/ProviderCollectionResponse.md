# ProviderCollectionResponse

Provider Collection serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**providers** | [**List[ProviderResponse]**](ProviderResponse.md) |  | 
**total_entries** | **int** |  | 

## Example

```python
from airflow_client.client.models.provider_collection_response import ProviderCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderCollectionResponse from a JSON string
provider_collection_response_instance = ProviderCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(ProviderCollectionResponse.to_json())

# convert the object into a dict
provider_collection_response_dict = provider_collection_response_instance.to_dict()
# create an instance of ProviderCollectionResponse from a dict
provider_collection_response_from_dict = ProviderCollectionResponse.from_dict(provider_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


