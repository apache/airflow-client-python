# ExtraLinkCollectionResponse

Extra Links Response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra_links** | **Dict[str, str]** |  | 
**total_entries** | **int** |  | 

## Example

```python
from airflow_client.client.models.extra_link_collection_response import ExtraLinkCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExtraLinkCollectionResponse from a JSON string
extra_link_collection_response_instance = ExtraLinkCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(ExtraLinkCollectionResponse.to_json())

# convert the object into a dict
extra_link_collection_response_dict = extra_link_collection_response_instance.to_dict()
# create an instance of ExtraLinkCollectionResponse from a dict
extra_link_collection_response_from_dict = ExtraLinkCollectionResponse.from_dict(extra_link_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


