# DAGRun


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conf** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | JSON object describing additional configuration parameters.  The value of this field can be set only when creating the object. If you try to modify the field of an existing object, the request fails with an BAD_REQUEST error.  | [optional] 
**dag_id** | **str** |  | [optional] [readonly] 
**dag_run_id** | **str, none_type** | Run ID.  The value of this field can be set only when creating the object. If you try to modify the field of an existing object, the request fails with an BAD_REQUEST error.  If not provided, a value will be generated based on execution_date.  If the specified dag_run_id is in use, the creation request fails with an ALREADY_EXISTS error.  This together with DAG_ID are a unique key.  | [optional] 
**data_interval_end** | **datetime, none_type** | The end of the interval the DAG run covers.  | [optional] 
**data_interval_start** | **datetime, none_type** | The beginning of the interval the DAG run covers.  | [optional] 
**end_date** | **datetime, none_type** |  | [optional] [readonly] 
**execution_date** | **datetime, none_type** | The execution date. This is the same as logical_date, kept for backwards compatibility. If both this field and logical_date are provided but with different values, the request will fail with an BAD_REQUEST error.  *Changed in version 2.2.0*&amp;#58; Field becomes nullable.  *Deprecated since version 2.2.0*&amp;#58; Use &#39;logical_date&#39; instead.  | [optional] 
**external_trigger** | **bool** |  | [optional] [readonly] 
**last_scheduling_decision** | **datetime, none_type** |  | [optional] [readonly] 
**logical_date** | **datetime, none_type** | The logical date (previously called execution date). This is the time or interval covered by this DAG run, according to the DAG definition.  The value of this field can be set only when creating the object. If you try to modify the field of an existing object, the request fails with an BAD_REQUEST error.  This together with DAG_ID are a unique key.  *New in version 2.2.0*  | [optional] 
**note** | **str, none_type** | Contains manually entered notes by the user about the DagRun.  *New in version 2.5.0*  | [optional] 
**run_type** | **str** |  | [optional] [readonly] 
**start_date** | **datetime, none_type** | The start time. The time when DAG run was actually created.  *Changed in version 2.1.3*&amp;#58; Field becomes nullable.  | [optional] [readonly] 
**state** | [**DagState**](DagState.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


