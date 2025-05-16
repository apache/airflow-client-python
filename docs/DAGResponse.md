# DAGResponse

DAG serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bundle_name** | **str** |  | [optional] 
**bundle_version** | **str** |  | [optional] 
**dag_display_name** | **str** |  | 
**dag_id** | **str** |  | 
**description** | **str** |  | [optional] 
**file_token** | **str** | Return file token. | [readonly] 
**fileloc** | **str** |  | 
**has_import_errors** | **bool** |  | 
**has_task_concurrency_limits** | **bool** |  | 
**is_paused** | **bool** |  | 
**is_stale** | **bool** |  | 
**last_expired** | **datetime** |  | [optional] 
**last_parsed_time** | **datetime** |  | [optional] 
**max_active_runs** | **int** |  | [optional] 
**max_active_tasks** | **int** |  | 
**max_consecutive_failed_dag_runs** | **int** |  | 
**next_dagrun_data_interval_end** | **datetime** |  | [optional] 
**next_dagrun_data_interval_start** | **datetime** |  | [optional] 
**next_dagrun_logical_date** | **datetime** |  | [optional] 
**next_dagrun_run_after** | **datetime** |  | [optional] 
**owners** | **List[str]** |  | 
**relative_fileloc** | **str** |  | [optional] 
**tags** | [**List[DagTagResponse]**](DagTagResponse.md) |  | 
**timetable_description** | **str** |  | [optional] 
**timetable_summary** | **str** |  | [optional] 

## Example

```python
from airflow_client.client.models.dag_response import DAGResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DAGResponse from a JSON string
dag_response_instance = DAGResponse.from_json(json)
# print the JSON string representation of the object
print(DAGResponse.to_json())

# convert the object into a dict
dag_response_dict = dag_response_instance.to_dict()
# create an instance of DAGResponse from a dict
dag_response_from_dict = DAGResponse.from_dict(dag_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


