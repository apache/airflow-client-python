# DAGResponse

Dag serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_id** | **str** |  | 
**dag_display_name** | **str** |  | 
**is_paused** | **bool** |  | 
**is_stale** | **bool** |  | 
**last_parsed_time** | **datetime** |  | 
**last_parse_duration** | **float** |  | 
**last_expired** | **datetime** |  | 
**bundle_name** | **str** |  | 
**bundle_version** | **str** |  | 
**relative_fileloc** | **str** |  | 
**fileloc** | **str** |  | 
**description** | **str** |  | 
**timetable_summary** | **str** |  | 
**timetable_description** | **str** |  | 
**timetable_partitioned** | **bool** |  | 
**tags** | [**List[DagTagResponse]**](DagTagResponse.md) |  | 
**max_active_tasks** | **int** |  | 
**max_active_runs** | **int** |  | 
**max_consecutive_failed_dag_runs** | **int** |  | 
**has_task_concurrency_limits** | **bool** |  | 
**has_import_errors** | **bool** |  | 
**next_dagrun_logical_date** | **datetime** |  | 
**next_dagrun_data_interval_start** | **datetime** |  | 
**next_dagrun_data_interval_end** | **datetime** |  | 
**next_dagrun_run_after** | **datetime** |  | 
**allowed_run_types** | [**List[DagRunType]**](DagRunType.md) |  | 
**owners** | **List[str]** |  | 
**file_token** | **str** | Return file token. | [readonly] 

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


