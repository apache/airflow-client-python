# TaskInstance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_id** | **str** |  | [optional] 
**dag_run_id** | **str** | The DagRun ID for this task instance  *New in version 2.3.0*  | [optional] 
**duration** | **float, none_type** |  | [optional] 
**end_date** | **str, none_type** |  | [optional] 
**execution_date** | **str** |  | [optional] 
**executor** | **str, none_type** | Executor the task is configured to run on or None (which indicates the default executor)  *New in version 2.10.0*  | [optional] 
**executor_config** | **str** |  | [optional] 
**hostname** | **str** |  | [optional] 
**map_index** | **int** |  | [optional] 
**max_tries** | **int** |  | [optional] 
**note** | **str, none_type** | Contains manually entered notes by the user about the TaskInstance.  *New in version 2.5.0*  | [optional] 
**operator** | **str, none_type** | *Changed in version 2.1.1*&amp;#58; Field becomes nullable.  | [optional] 
**pid** | **int, none_type** |  | [optional] 
**pool** | **str** |  | [optional] 
**pool_slots** | **int** |  | [optional] 
**priority_weight** | **int, none_type** |  | [optional] 
**queue** | **str, none_type** |  | [optional] 
**queued_when** | **str, none_type** | The datetime that the task enter the state QUEUE, also known as queue_at  | [optional] 
**rendered_fields** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | JSON object describing rendered fields.  *New in version 2.3.0*  | [optional] 
**rendered_map_index** | **str, none_type** | Rendered name of an expanded task instance, if the task is mapped.  *New in version 2.9.0*  | [optional] 
**sla_miss** | [**SLAMiss**](SLAMiss.md) |  | [optional] 
**start_date** | **str, none_type** |  | [optional] 
**state** | [**TaskState**](TaskState.md) |  | [optional] 
**task_display_name** | **str** | Human centric display text for the task.  *New in version 2.9.0*  | [optional] 
**task_id** | **str** |  | [optional] 
**trigger** | [**Trigger**](Trigger.md) |  | [optional] 
**triggerer_job** | [**Job**](Job.md) |  | [optional] 
**try_number** | **int** |  | [optional] 
**unixname** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


