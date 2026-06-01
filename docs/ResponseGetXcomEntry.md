# ResponseGetXcomEntry


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
**value** | **str** |  | 

## Example

```python
from airflow_client.client.models.response_get_xcom_entry import ResponseGetXcomEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetXcomEntry from a JSON string
response_get_xcom_entry_instance = ResponseGetXcomEntry.from_json(json)
# print the JSON string representation of the object
print(ResponseGetXcomEntry.to_json())

# convert the object into a dict
response_get_xcom_entry_dict = response_get_xcom_entry_instance.to_dict()
# create an instance of ResponseGetXcomEntry from a dict
response_get_xcom_entry_from_dict = ResponseGetXcomEntry.from_dict(response_get_xcom_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


