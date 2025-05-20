# ResponseClearDagRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_instances** | [**List[TaskInstanceResponse]**](TaskInstanceResponse.md) |  | 
**total_entries** | **int** |  | 
**bundle_version** | **str** |  | [optional] 
**conf** | **object** |  | 
**dag_id** | **str** |  | 
**dag_run_id** | **str** |  | 
**dag_versions** | [**List[DagVersionResponse]**](DagVersionResponse.md) |  | 
**data_interval_end** | **datetime** |  | [optional] 
**data_interval_start** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**last_scheduling_decision** | **datetime** |  | [optional] 
**logical_date** | **datetime** |  | [optional] 
**note** | **str** |  | [optional] 
**queued_at** | **datetime** |  | [optional] 
**run_after** | **datetime** |  | 
**run_type** | [**DagRunType**](DagRunType.md) |  | 
**start_date** | **datetime** |  | [optional] 
**state** | [**DagRunState**](DagRunState.md) |  | 
**triggered_by** | [**DagRunTriggeredByType**](DagRunTriggeredByType.md) |  | [optional] 

## Example

```python
from airflow_client.client.models.response_clear_dag_run import ResponseClearDagRun

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseClearDagRun from a JSON string
response_clear_dag_run_instance = ResponseClearDagRun.from_json(json)
# print the JSON string representation of the object
print(ResponseClearDagRun.to_json())

# convert the object into a dict
response_clear_dag_run_dict = response_clear_dag_run_instance.to_dict()
# create an instance of ResponseClearDagRun from a dict
response_clear_dag_run_from_dict = ResponseClearDagRun.from_dict(response_clear_dag_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


