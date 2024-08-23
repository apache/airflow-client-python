# EventLog

Log of user operations via CLI or Web UI.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_id** | **str, none_type** | The DAG ID | [optional] [readonly] 
**event** | **str** | A key describing the type of event. | [optional] [readonly] 
**event_log_id** | **int** | The event log ID | [optional] [readonly] 
**execution_date** | **datetime, none_type** | When the event was dispatched for an object having execution_date, the value of this field.  | [optional] [readonly] 
**extra** | **str, none_type** | Other information that was not included in the other fields, e.g. the complete CLI command.  | [optional] [readonly] 
**map_index** | **int, none_type** | The Map Index | [optional] [readonly] 
**owner** | **str, none_type** | Name of the user who triggered these events a. | [optional] [readonly] 
**run_id** | **str, none_type** | The DAG Run ID | [optional] [readonly] 
**task_id** | **str, none_type** | The Task ID | [optional] [readonly] 
**try_number** | **int, none_type** | The Try Number | [optional] [readonly] 
**when** | **datetime** | The time when these events happened. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


