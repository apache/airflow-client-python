# UpdateTaskState

Expected new state. Only a subset of TaskState are available.  Other states are managed directly by the scheduler or the workers and cannot be updated manually through the REST API. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Expected new state. Only a subset of TaskState are available.  Other states are managed directly by the scheduler or the workers and cannot be updated manually through the REST API.  |  must be one of ["success", "failed", "skipped", ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


