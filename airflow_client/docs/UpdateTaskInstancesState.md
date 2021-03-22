# UpdateTaskInstancesState

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **bool** | If set, don&#39;t actually run this operation. The response will contain a list of task instances planned to be affected, but won&#39;t be modified in any way.  | [optional]  if omitted the server will use the default value of True
**task_id** | **str** | The task ID. | [optional] 
**execution_date** | **str** | The execution date. | [optional] 
**include_upstream** | **bool** | If set to true, upstream tasks are also affected. | [optional] 
**include_downstream** | **bool** | If set to true, downstream tasks are also affected. | [optional] 
**include_future** | **bool** | If set to True, also tasks from future DAG Runs are affected. | [optional] 
**include_past** | **bool** | If set to True, also tasks from past DAG Runs are affected. | [optional] 
**new_state** | **str** | Expected new state. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


