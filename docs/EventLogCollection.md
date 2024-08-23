# EventLogCollection

Collection of event logs.  *Changed in version 2.1.0*&#58; 'total_entries' field is added. *Changed in version 2.10.0*&#58; 'try_number' and 'map_index' fields are added. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_logs** | [**[EventLog]**](EventLog.md) |  | [optional] 
**total_entries** | **int** | Count of total objects in the current result set before pagination parameters (limit, offset) are applied.  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


