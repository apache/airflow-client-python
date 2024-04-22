# DatasetEvent

A dataset event.  *New in version 2.4.0* 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_dagruns** | [**[BasicDAGRun]**](BasicDAGRun.md) |  | [optional] 
**dataset_id** | **int** | The dataset id | [optional] 
**dataset_uri** | **str** | The URI of the dataset | [optional] 
**extra** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | The dataset event extra | [optional] 
**source_dag_id** | **str, none_type** | The DAG ID that updated the dataset. | [optional] 
**source_map_index** | **int, none_type** | The task map index that updated the dataset. | [optional] 
**source_run_id** | **str, none_type** | The DAG run ID that updated the dataset. | [optional] 
**source_task_id** | **str, none_type** | The task ID that updated the dataset. | [optional] 
**timestamp** | **str** | The dataset event creation time | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


