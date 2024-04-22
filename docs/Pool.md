# Pool

The pool

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deferred_slots** | **int** | The number of slots used by deferred tasks at the moment. Relevant if &#39;include_deferred&#39; is set to true.  *New in version 2.7.0*  | [optional] [readonly] 
**description** | **str, none_type** | The description of the pool.  *New in version 2.3.0*  | [optional] 
**include_deferred** | **bool** | If set to true, deferred tasks are considered when calculating open pool slots.  *New in version 2.7.0*  | [optional] 
**name** | **str** | The name of pool. | [optional] 
**occupied_slots** | **int** | The number of slots used by running/queued tasks at the moment. May include deferred tasks if &#39;include_deferred&#39; is set to true. | [optional] [readonly] 
**open_slots** | **int** | The number of free slots at the moment. | [optional] [readonly] 
**queued_slots** | **int** | The number of slots used by queued tasks at the moment. | [optional] [readonly] 
**running_slots** | **int** | The number of slots used by running tasks at the moment. | [optional] [readonly] 
**scheduled_slots** | **int** | The number of slots used by scheduled tasks at the moment. | [optional] [readonly] 
**slots** | **int** | The maximum number of slots that can be assigned to tasks. One job may occupy one or more slots.  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


