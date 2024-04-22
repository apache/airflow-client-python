# ListDagRunsForm


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_ids** | **[str]** | Return objects with specific DAG IDs. The value can be repeated to retrieve multiple matching values (OR condition). | [optional] 
**end_date_gte** | **datetime** | Returns objects greater or equal the specified date.  This can be combined with end_date_lte parameter to receive only the selected period.  | [optional] 
**end_date_lte** | **datetime** | Returns objects less than or equal to the specified date.  This can be combined with end_date_gte parameter to receive only the selected period.  | [optional] 
**execution_date_gte** | **datetime** | Returns objects greater or equal to the specified date.  This can be combined with execution_date_lte key to receive only the selected period.  | [optional] 
**execution_date_lte** | **datetime** | Returns objects less than or equal to the specified date.  This can be combined with execution_date_gte key to receive only the selected period.  | [optional] 
**order_by** | **str** | The name of the field to order the results by. Prefix a field name with &#x60;-&#x60; to reverse the sort order.  *New in version 2.1.0*  | [optional] 
**page_limit** | **int** | The numbers of items to return. | [optional]  if omitted the server will use the default value of 100
**page_offset** | **int** | The number of items to skip before starting to collect the result set. | [optional] 
**start_date_gte** | **datetime** | Returns objects greater or equal the specified date.  This can be combined with start_date_lte key to receive only the selected period.  | [optional] 
**start_date_lte** | **datetime** | Returns objects less or equal the specified date.  This can be combined with start_date_gte parameter to receive only the selected period  | [optional] 
**states** | **[str]** | Return objects with specific states. The value can be repeated to retrieve multiple matching values (OR condition). | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


