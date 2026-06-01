# TaskResponse

Task serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** |  | 
**task_display_name** | **str** |  | 
**owner** | **str** |  | 
**start_date** | **datetime** |  | 
**end_date** | **datetime** |  | 
**trigger_rule** | **str** |  | 
**depends_on_past** | **bool** |  | 
**wait_for_downstream** | **bool** |  | 
**retries** | **float** |  | 
**queue** | **str** |  | 
**pool** | **str** |  | 
**pool_slots** | **float** |  | 
**execution_timeout** | [**TimeDelta**](TimeDelta.md) |  | 
**retry_delay** | [**TimeDelta**](TimeDelta.md) |  | 
**retry_exponential_backoff** | **float** |  | 
**priority_weight** | **float** |  | 
**weight_rule** | **str** |  | 
**ui_color** | **str** |  | 
**ui_fgcolor** | **str** |  | 
**template_fields** | **List[str]** |  | 
**downstream_task_ids** | **List[str]** |  | 
**doc_md** | **str** |  | 
**operator_name** | **str** |  | 
**params** | **Dict[str, object]** |  | 
**class_ref** | **Dict[str, object]** |  | 
**is_mapped** | **bool** |  | 
**extra_links** | **List[str]** | Extract and return extra_links. | [readonly] 

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


