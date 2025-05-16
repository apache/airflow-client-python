# XComUpdateBody

Payload serializer for updating an XCom entry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**map_index** | **int** |  | [optional] [default to -1]
**value** | **object** |  | 

## Example

```python
from airflow_client.client.models.x_com_update_body import XComUpdateBody

# TODO update the JSON string below
json = "{}"
# create an instance of XComUpdateBody from a JSON string
x_com_update_body_instance = XComUpdateBody.from_json(json)
# print the JSON string representation of the object
print(XComUpdateBody.to_json())

# convert the object into a dict
x_com_update_body_dict = x_com_update_body_instance.to_dict()
# create an instance of XComUpdateBody from a dict
x_com_update_body_from_dict = XComUpdateBody.from_dict(x_com_update_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


