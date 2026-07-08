# AssetEventAccessControl

Access control settings for asset event consumer team filtering.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_global** | **bool** |  | [optional] [default to True]
**consumer_teams** | **List[str]** |  | [optional] 

## Example

```python
from airflow_client.client.models.asset_event_access_control import AssetEventAccessControl

# TODO update the JSON string below
json = "{}"
# create an instance of AssetEventAccessControl from a JSON string
asset_event_access_control_instance = AssetEventAccessControl.from_json(json)
# print the JSON string representation of the object
print(AssetEventAccessControl.to_json())

# convert the object into a dict
asset_event_access_control_dict = asset_event_access_control_instance.to_dict()
# create an instance of AssetEventAccessControl from a dict
asset_event_access_control_from_dict = AssetEventAccessControl.from_dict(asset_event_access_control_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


