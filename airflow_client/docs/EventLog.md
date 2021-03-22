# EventLog

Log of user operations via CLI or Web UI.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_log_id** | **int** | The evnet log ID | [optional] [readonly] 
**when** | **datetime** | The time when these events happened. | [optional] [readonly] 
**dag_id** | **str, none_type** | The DAG ID | [optional] [readonly] 
**task_id** | **str, none_type** | The DAG ID | [optional] [readonly] 
**event** | **str** | A key describing the type of event. | [optional] [readonly] 
**execution_date** | **datetime, none_type** | When the event was dispatched for an object having execution_date, the value of this field.  | [optional] [readonly] 
**owner** | **str** | Name of the user who triggered these events a. | [optional] [readonly] 
**extra** | **str, none_type** | Other information that was not included in the other fields, e.g. the complete CLI command.  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


