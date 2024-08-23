# ListTaskInstanceForm


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_ids** | **[str]** | Return objects with specific DAG IDs. The value can be repeated to retrieve multiple matching values (OR condition). | [optional] 
**dag_run_ids** | **[str]** | Return objects with specific DAG Run IDs. The value can be repeated to retrieve multiple matching values (OR condition). *New in version 2.7.1* | [optional] 
**duration_gte** | **float** | Returns objects greater than or equal to the specified values.  This can be combined with duration_lte parameter to receive only the selected period.  | [optional] 
**duration_lte** | **float** | Returns objects less than or equal to the specified values.  This can be combined with duration_gte parameter to receive only the selected range.  | [optional] 
**end_date_gte** | **datetime** | Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period.  | [optional] 
**end_date_lte** | **datetime** | Returns objects less than or equal to the specified date.  This can be combined with start_date_gte parameter to receive only the selected period.  | [optional] 
**execution_date_gte** | **datetime** | Returns objects greater or equal to the specified date.  This can be combined with execution_date_lte parameter to receive only the selected period.  | [optional] 
**execution_date_lte** | **datetime** | Returns objects less than or equal to the specified date.  This can be combined with execution_date_gte parameter to receive only the selected period.  | [optional] 
**executor** | **[str]** | The value can be repeated to retrieve multiple matching values (OR condition). | [optional] 
**pool** | **[str]** | The value can be repeated to retrieve multiple matching values (OR condition). | [optional] 
**queue** | **[str]** | The value can be repeated to retrieve multiple matching values (OR condition). | [optional] 
**start_date_gte** | **datetime** | Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period.  | [optional] 
**start_date_lte** | **datetime** | Returns objects less or equal the specified date.  This can be combined with start_date_gte parameter to receive only the selected period.  | [optional] 
**state** | [**[TaskState]**](TaskState.md) | The value can be repeated to retrieve multiple matching values (OR condition). | [optional] 
**task_ids** | **[str]** | Return objects with specific task IDs. The value can be repeated to retrieve multiple matching values (OR condition). *New in version 2.7.1* | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


