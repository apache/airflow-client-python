# XComResponseString

XCom response serializer with string return type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_id** | **str** |  | 
**key** | **str** |  | 
**logical_date** | **datetime** |  | [optional] 
**map_index** | **int** |  | 
**run_id** | **str** |  | 
**task_id** | **str** |  | 
**timestamp** | **datetime** |  | 
**value** | **str** |  | [optional] 

## Example

```python
from airflow_client.client.models.x_com_response_string import XComResponseString

# TODO update the JSON string below
json = "{}"
# create an instance of XComResponseString from a JSON string
x_com_response_string_instance = XComResponseString.from_json(json)
# print the JSON string representation of the object
print(XComResponseString.to_json())

# convert the object into a dict
x_com_response_string_dict = x_com_response_string_instance.to_dict()
# create an instance of XComResponseString from a dict
x_com_response_string_from_dict = XComResponseString.from_dict(x_com_response_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


