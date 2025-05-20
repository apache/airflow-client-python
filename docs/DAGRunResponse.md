# DAGRunResponse

DAG Run serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bundle_version** | **str** |  | [optional] 
**conf** | **object** |  | 
**dag_id** | **str** |  | 
**dag_run_id** | **str** |  | 
**dag_versions** | [**List[DagVersionResponse]**](DagVersionResponse.md) |  | 
**data_interval_end** | **datetime** |  | [optional] 
**data_interval_start** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**last_scheduling_decision** | **datetime** |  | [optional] 
**logical_date** | **datetime** |  | [optional] 
**note** | **str** |  | [optional] 
**queued_at** | **datetime** |  | [optional] 
**run_after** | **datetime** |  | 
**run_type** | [**DagRunType**](DagRunType.md) |  | 
**start_date** | **datetime** |  | [optional] 
**state** | [**DagRunState**](DagRunState.md) |  | 
**triggered_by** | [**DagRunTriggeredByType**](DagRunTriggeredByType.md) |  | [optional] 

## Example

```python
from airflow_client.client.models.dag_run_response import DAGRunResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DAGRunResponse from a JSON string
dag_run_response_instance = DAGRunResponse.from_json(json)
# print the JSON string representation of the object
print(DAGRunResponse.to_json())

# convert the object into a dict
dag_run_response_dict = dag_run_response_instance.to_dict()
# create an instance of DAGRunResponse from a dict
dag_run_response_from_dict = DAGRunResponse.from_dict(dag_run_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


