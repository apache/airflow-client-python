# DAGDetailsResponse

Specific serializer for DAG Details responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_expression** | **object** |  | [optional] 
**bundle_name** | **str** |  | [optional] 
**bundle_version** | **str** |  | [optional] 
**catchup** | **bool** |  | 
**concurrency** | **int** | Return max_active_tasks as concurrency. | [readonly] 
**dag_display_name** | **str** |  | 
**dag_id** | **str** |  | 
**dag_run_timeout** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**doc_md** | **str** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**file_token** | **str** | Return file token. | [readonly] 
**fileloc** | **str** |  | 
**has_import_errors** | **bool** |  | 
**has_task_concurrency_limits** | **bool** |  | 
**is_paused** | **bool** |  | 
**is_paused_upon_creation** | **bool** |  | [optional] 
**is_stale** | **bool** |  | 
**last_expired** | **datetime** |  | [optional] 
**last_parsed** | **datetime** |  | [optional] 
**last_parsed_time** | **datetime** |  | [optional] 
**latest_dag_version** | [**DagVersionResponse**](DagVersionResponse.md) |  | [optional] 
**max_active_runs** | **int** |  | [optional] 
**max_active_tasks** | **int** |  | 
**max_consecutive_failed_dag_runs** | **int** |  | 
**next_dagrun_data_interval_end** | **datetime** |  | [optional] 
**next_dagrun_data_interval_start** | **datetime** |  | [optional] 
**next_dagrun_logical_date** | **datetime** |  | [optional] 
**next_dagrun_run_after** | **datetime** |  | [optional] 
**owner_links** | **Dict[str, str]** |  | [optional] 
**owners** | **List[str]** |  | 
**params** | **object** |  | [optional] 
**relative_fileloc** | **str** |  | [optional] 
**render_template_as_native_obj** | **bool** |  | 
**start_date** | **datetime** |  | [optional] 
**tags** | [**List[DagTagResponse]**](DagTagResponse.md) |  | 
**template_search_path** | **List[str]** |  | [optional] 
**timetable_description** | **str** |  | [optional] 
**timetable_summary** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 

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


