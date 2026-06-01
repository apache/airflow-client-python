# XComResponse

Serializer for a xcom item.

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

## Example

```python
from airflow_client.client.models.x_com_response import XComResponse

# TODO update the JSON string below
json = "{}"
# create an instance of XComResponse from a JSON string
x_com_response_instance = XComResponse.from_json(json)
# print the JSON string representation of the object
print(XComResponse.to_json())

# convert the object into a dict
x_com_response_dict = x_com_response_instance.to_dict()
# create an instance of XComResponse from a dict
x_com_response_from_dict = XComResponse.from_dict(x_com_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


