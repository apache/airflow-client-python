# AssetEventCollectionResponse

Asset event collection response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_events** | [**List[AssetEventResponse]**](AssetEventResponse.md) |  | 
**total_entries** | **int** |  | 

## Example

```python
from airflow_client.client.models.asset_event_collection_response import AssetEventCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssetEventCollectionResponse from a JSON string
asset_event_collection_response_instance = AssetEventCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(AssetEventCollectionResponse.to_json())

# convert the object into a dict
asset_event_collection_response_dict = asset_event_collection_response_instance.to_dict()
# create an instance of AssetEventCollectionResponse from a dict
asset_event_collection_response_from_dict = AssetEventCollectionResponse.from_dict(asset_event_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


