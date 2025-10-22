# LastAssetEventResponse

Last asset event response serializer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 

## Example

```python
from airflow_client.client.models.last_asset_event_response import LastAssetEventResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LastAssetEventResponse from a JSON string
last_asset_event_response_instance = LastAssetEventResponse.from_json(json)
# print the JSON string representation of the object
print(LastAssetEventResponse.to_json())

# convert the object into a dict
last_asset_event_response_dict = last_asset_event_response_instance.to_dict()
# create an instance of LastAssetEventResponse from a dict
last_asset_event_response_from_dict = LastAssetEventResponse.from_dict(last_asset_event_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


