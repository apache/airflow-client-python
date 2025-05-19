# DAGRunsBatchBody

List DAG Runs body for batch endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_ids** | **List[str]** |  | [optional] 
**end_date_gte** | **datetime** |  | [optional] 
**end_date_lte** | **datetime** |  | [optional] 
**logical_date_gte** | **datetime** |  | [optional] 
**logical_date_lte** | **datetime** |  | [optional] 
**order_by** | **str** |  | [optional] 
**page_limit** | **int** |  | [optional] [default to 100]
**page_offset** | **int** |  | [optional] [default to 0]
**run_after_gte** | **datetime** |  | [optional] 
**run_after_lte** | **datetime** |  | [optional] 
**start_date_gte** | **datetime** |  | [optional] 
**start_date_lte** | **datetime** |  | [optional] 
**states** | [**List[Optional[DagRunState]]**](DagRunState.md) |  | [optional] 

## Example

```python
from airflow_client.client.models.dag_runs_batch_body import DAGRunsBatchBody

# TODO update the JSON string below
json = "{}"
# create an instance of DAGRunsBatchBody from a JSON string
dag_runs_batch_body_instance = DAGRunsBatchBody.from_json(json)
# print the JSON string representation of the object
print(DAGRunsBatchBody.to_json())

# convert the object into a dict
dag_runs_batch_body_dict = dag_runs_batch_body_instance.to_dict()
# create an instance of DAGRunsBatchBody from a dict
dag_runs_batch_body_from_dict = DAGRunsBatchBody.from_dict(dag_runs_batch_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


