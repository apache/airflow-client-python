# XComCreateBody

Payload serializer for creating an XCom entry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**map_index** | **int** |  | [optional] [default to -1]
**value** | **object** |  | 

## Example

```python
from airflow_client.client.models.x_com_create_body import XComCreateBody

# TODO update the JSON string below
json = "{}"
# create an instance of XComCreateBody from a JSON string
x_com_create_body_instance = XComCreateBody.from_json(json)
# print the JSON string representation of the object
print(XComCreateBody.to_json())

# convert the object into a dict
x_com_create_body_dict = x_com_create_body_instance.to_dict()
# create an instance of XComCreateBody from a dict
x_com_create_body_from_dict = XComCreateBody.from_dict(x_com_create_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


