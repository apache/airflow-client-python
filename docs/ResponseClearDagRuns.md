# ResponseClearDagRuns


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_instances** | [**List[TaskInstancesInner]**](TaskInstancesInner.md) |  | 
**total_entries** | **int** |  | 
**dag_runs** | [**List[DAGRunResponse]**](DAGRunResponse.md) |  | 
**next_cursor** | **str** |  | [optional] 
**previous_cursor** | **str** |  | [optional] 

## Example

```python
from airflow_client.client.models.response_clear_dag_runs import ResponseClearDagRuns

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseClearDagRuns from a JSON string
response_clear_dag_runs_instance = ResponseClearDagRuns.from_json(json)
# print the JSON string representation of the object
print(ResponseClearDagRuns.to_json())

# convert the object into a dict
response_clear_dag_runs_dict = response_clear_dag_runs_instance.to_dict()
# create an instance of ResponseClearDagRuns from a dict
response_clear_dag_runs_from_dict = ResponseClearDagRuns.from_dict(response_clear_dag_runs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


