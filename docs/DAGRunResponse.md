# DAGRunResponse

Dag Run serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_run_id** | **str** |  | 
**dag_id** | **str** |  | 
**logical_date** | **datetime** |  | 
**queued_at** | **datetime** |  | 
**start_date** | **datetime** |  | 
**end_date** | **datetime** |  | 
**duration** | **float** |  | 
**data_interval_start** | **datetime** |  | 
**data_interval_end** | **datetime** |  | 
**run_after** | **datetime** |  | 
**last_scheduling_decision** | **datetime** |  | 
**run_type** | [**DagRunType**](DagRunType.md) |  | 
**state** | [**DagRunState**](DagRunState.md) |  | 
**triggered_by** | [**DagRunTriggeredByType**](DagRunTriggeredByType.md) |  | 
**triggering_user_name** | **str** |  | 
**conf** | **Dict[str, object]** |  | 
**note** | **str** |  | 
**dag_versions** | [**List[DagVersionResponse]**](DagVersionResponse.md) |  | 
**bundle_version** | **str** |  | 
**dag_display_name** | **str** |  | 
**partition_key** | **str** |  | 

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


