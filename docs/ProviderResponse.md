# ProviderResponse

Provider serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**package_name** | **str** |  | 
**version** | **str** |  | 

## Example

```python
from airflow_client.client.models.provider_response import ProviderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderResponse from a JSON string
provider_response_instance = ProviderResponse.from_json(json)
# print the JSON string representation of the object
print(ProviderResponse.to_json())

# convert the object into a dict
provider_response_dict = provider_response_instance.to_dict()
# create an instance of ProviderResponse from a dict
provider_response_from_dict = ProviderResponse.from_dict(provider_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


