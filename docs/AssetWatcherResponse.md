# AssetWatcherResponse

Asset watcher serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_date** | **datetime** |  | 
**name** | **str** |  | 
**trigger_id** | **int** |  | 

## Example

```python
from airflow_client.client.models.asset_watcher_response import AssetWatcherResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssetWatcherResponse from a JSON string
asset_watcher_response_instance = AssetWatcherResponse.from_json(json)
# print the JSON string representation of the object
print(AssetWatcherResponse.to_json())

# convert the object into a dict
asset_watcher_response_dict = asset_watcher_response_instance.to_dict()
# create an instance of AssetWatcherResponse from a dict
asset_watcher_response_from_dict = AssetWatcherResponse.from_dict(asset_watcher_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


