# Pool

The pool

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of pool. | [optional] 
**slots** | **int** | The maximum number of slots that can be assigned to tasks. One job may occupy one or more slots.  | [optional] 
**occupied_slots** | **int** | The number of slots used by running/queued tasks at the moment. | [optional] [readonly] 
**used_slots** | **int** | The number of slots used by running tasks at the moment. | [optional] [readonly] 
**queued_slots** | **int** | The number of slots used by queued tasks at the moment. | [optional] [readonly] 
**open_slots** | **int** | The number of free slots at the moment. | [optional] [readonly] 
**description** | **str, none_type** | The description of the pool.  *New in version 2.3.0*  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


