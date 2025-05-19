# CreateAssetEventsBody

Create asset events request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **int** |  | 
**extra** | **object** |  | [optional] 

## Example

```python
from airflow_client.client.models.create_asset_events_body import CreateAssetEventsBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAssetEventsBody from a JSON string
create_asset_events_body_instance = CreateAssetEventsBody.from_json(json)
# print the JSON string representation of the object
print(CreateAssetEventsBody.to_json())

# convert the object into a dict
create_asset_events_body_dict = create_asset_events_body_instance.to_dict()
# create an instance of CreateAssetEventsBody from a dict
create_asset_events_body_from_dict = CreateAssetEventsBody.from_dict(create_asset_events_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


