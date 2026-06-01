# XComResponseNative

XCom response serializer with native return type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**timestamp** | **datetime** |  | 
**logical_date** | **datetime** |  | 
**map_index** | **int** |  | 
**task_id** | **str** |  | 
**dag_id** | **str** |  | 
**run_id** | **str** |  | 
**dag_display_name** | **str** |  | 
**task_display_name** | **str** |  | 
**run_after** | **datetime** |  | 
**value** | **object** |  | 

## Example

```python
from airflow_client.client.models.x_com_response_native import XComResponseNative

# TODO update the JSON string below
json = "{}"
# create an instance of XComResponseNative from a JSON string
x_com_response_native_instance = XComResponseNative.from_json(json)
# print the JSON string representation of the object
print(XComResponseNative.to_json())

# convert the object into a dict
x_com_response_native_dict = x_com_response_native_instance.to_dict()
# create an instance of XComResponseNative from a dict
x_com_response_native_from_dict = XComResponseNative.from_dict(x_com_response_native_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


