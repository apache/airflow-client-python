# TaskInstance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** |  | [optional] 
**dag_id** | **str** |  | [optional] 
**dag_run_id** | **str** | The DagRun ID for this task instance  *New in version 2.3.0*  | [optional] 
**execution_date** | **str** |  | [optional] 
**start_date** | **str, none_type** |  | [optional] 
**end_date** | **str, none_type** |  | [optional] 
**duration** | **float, none_type** |  | [optional] 
**state** | [**TaskState**](TaskState.md) |  | [optional] 
**try_number** | **int** |  | [optional] 
**max_tries** | **int** |  | [optional] 
**hostname** | **str** |  | [optional] 
**unixname** | **str** |  | [optional] 
**pool** | **str** |  | [optional] 
**pool_slots** | **int** |  | [optional] 
**queue** | **str** |  | [optional] 
**priority_weight** | **int** |  | [optional] 
**operator** | **str, none_type** | *Changed in version 2.1.1*&amp;#58; Field becomes nullable.  | [optional] 
**queued_when** | **str, none_type** |  | [optional] 
**pid** | **int, none_type** |  | [optional] 
**executor_config** | **str** |  | [optional] 
**sla_miss** | [**SLAMiss**](SLAMiss.md) |  | [optional] 
**rendered_fields** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | JSON object describing rendered fields.  *New in version 2.3.0*  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


