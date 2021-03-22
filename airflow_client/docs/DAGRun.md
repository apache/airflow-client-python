# DAGRun

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_id** | **str** |  | [readonly] 
**dag_run_id** | **str, none_type** | Run ID.  The value of this field can be set only when creating the object. If you try to modify the field of an existing object, the request fails with an BAD_REQUEST error.  If not provided, a value will be generated based on execution_date.  If the specified dag_run_id is in use, the creation request fails with an ALREADY_EXISTS error.  This together with DAG_ID are a unique key.  | [optional] 
**execution_date** | **datetime** | The execution date. This is the time when the DAG run should be started according to the DAG definition. The value of this field can be set only when creating the object. If you try to modify the field of an existing object, the request fails with an BAD_REQUEST error. This together with DAG_ID are a unique key.  | [optional] 
**start_date** | **datetime** | The start time. The time when DAG run was actually created.  | [optional] [readonly] 
**end_date** | **datetime, none_type** |  | [optional] [readonly] 
**state** | [**DagState**](DagState.md) |  | [optional] 
**external_trigger** | **bool** |  | [optional] [readonly]  if omitted the server will use the default value of True
**conf** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | JSON object describing additional configuration parameters.  The value of this field can be set only when creating the object. If you try to modify the field of an existing object, the request fails with an BAD_REQUEST error.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


