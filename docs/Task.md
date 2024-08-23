# Task

For details see: [airflow.models.baseoperator.BaseOperator](https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/models/baseoperator/index.html#airflow.models.baseoperator.BaseOperator) 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_ref** | [**ClassReference**](ClassReference.md) |  | [optional] 
**depends_on_past** | **bool** |  | [optional] [readonly] 
**doc_md** | **str, none_type** | Task documentation in markdown.  *New in version 2.10.0*  | [optional] [readonly] 
**downstream_task_ids** | **[str]** |  | [optional] [readonly] 
**end_date** | **datetime, none_type** |  | [optional] [readonly] 
**execution_timeout** | [**TimeDelta**](TimeDelta.md) |  | [optional] 
**executor** | **str, none_type** |  | [optional] [readonly] 
**extra_links** | [**[TaskExtraLinks]**](TaskExtraLinks.md) |  | [optional] [readonly] 
**is_mapped** | **bool** |  | [optional] [readonly] 
**owner** | **str** |  | [optional] [readonly] 
**pool** | **str** |  | [optional] [readonly] 
**pool_slots** | **float** |  | [optional] [readonly] 
**priority_weight** | **float** |  | [optional] [readonly] 
**queue** | **str, none_type** |  | [optional] [readonly] 
**retries** | **float** |  | [optional] [readonly] 
**retry_delay** | [**TimeDelta**](TimeDelta.md) |  | [optional] 
**retry_exponential_backoff** | **bool** |  | [optional] [readonly] 
**start_date** | **datetime, none_type** |  | [optional] [readonly] 
**sub_dag** | [**DAG**](DAG.md) |  | [optional] 
**task_display_name** | **str** |  | [optional] [readonly] 
**task_id** | **str** |  | [optional] [readonly] 
**template_fields** | **[str]** |  | [optional] [readonly] 
**trigger_rule** | [**TriggerRule**](TriggerRule.md) |  | [optional] 
**ui_color** | [**Color**](Color.md) |  | [optional] 
**ui_fgcolor** | [**Color**](Color.md) |  | [optional] 
**wait_for_downstream** | **bool** |  | [optional] [readonly] 
**weight_rule** | [**WeightRule**](WeightRule.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


