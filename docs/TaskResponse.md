# TaskResponse

Task serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_ref** | **object** |  | [optional] 
**depends_on_past** | **bool** |  | 
**doc_md** | **str** |  | [optional] 
**downstream_task_ids** | **List[str]** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**execution_timeout** | [**TimeDelta**](TimeDelta.md) |  | [optional] 
**extra_links** | **List[str]** | Extract and return extra_links. | 
**is_mapped** | **bool** |  | [optional] 
**operator_name** | **str** |  | [optional] 
**owner** | **str** |  | [optional] 
**params** | **object** |  | [optional] 
**pool** | **str** |  | [optional] 
**pool_slots** | **float** |  | [optional] 
**priority_weight** | **float** |  | [optional] 
**queue** | **str** |  | [optional] 
**retries** | **float** |  | [optional] 
**retry_delay** | [**TimeDelta**](TimeDelta.md) |  | [optional] 
**retry_exponential_backoff** | **bool** |  | 
**start_date** | **datetime** |  | [optional] 
**task_display_name** | **str** |  | [optional] 
**task_id** | **str** |  | [optional] 
**template_fields** | **List[str]** |  | [optional] 
**trigger_rule** | **str** |  | [optional] 
**ui_color** | **str** |  | [optional] 
**ui_fgcolor** | **str** |  | [optional] 
**wait_for_downstream** | **bool** |  | 
**weight_rule** | **str** |  | [optional] 

## Example

```python
from airflow_client.client.models.task_response import TaskResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TaskResponse from a JSON string
task_response_instance = TaskResponse.from_json(json)
# print the JSON string representation of the object
print(TaskResponse.to_json())

# convert the object into a dict
task_response_dict = task_response_instance.to_dict()
# create an instance of TaskResponse from a dict
task_response_from_dict = TaskResponse.from_dict(task_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


