# DAGDetailsResponse

Specific serializer for Dag Details responses.

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
**catchup** | **bool** |  | 
**dag_run_timeout** | **str** |  | 
**asset_expression** | **Dict[str, object]** |  | 
**doc_md** | **str** |  | 
**start_date** | **datetime** |  | 
**end_date** | **datetime** |  | 
**is_paused_upon_creation** | **bool** |  | 
**params** | **Dict[str, object]** |  | 
**render_template_as_native_obj** | **bool** |  | 
**template_search_path** | **List[str]** |  | 
**timezone** | **str** |  | 
**last_parsed** | **datetime** |  | 
**default_args** | **Dict[str, object]** |  | 
**owner_links** | **Dict[str, str]** |  | [optional] 
**is_favorite** | **bool** |  | [optional] [default to False]
**active_runs_count** | **int** |  | [optional] [default to 0]
**file_token** | **str** | Return file token. | [readonly] 
**concurrency** | **int** | Return max_active_tasks as concurrency.  Deprecated: Use max_active_tasks instead. | [readonly] 
**latest_dag_version** | [**DagVersionResponse**](DagVersionResponse.md) | Return the latest DagVersion. | [readonly] 

## Example

```python
from airflow_client.client.models.dag_details_response import DAGDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DAGDetailsResponse from a JSON string
dag_details_response_instance = DAGDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(DAGDetailsResponse.to_json())

# convert the object into a dict
dag_details_response_dict = dag_details_response_instance.to_dict()
# create an instance of DAGDetailsResponse from a dict
dag_details_response_from_dict = DAGDetailsResponse.from_dict(dag_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


