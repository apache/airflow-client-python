# BackfillDagRunResponse

Serializer for a single BackfillDagRun entry with joined DagRun state.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backfill_id** | **int** |  | 
**dag_id** | **str** |  | 
**dag_run_id** | **str** |  | [optional] 
**dag_run_state** | [**DagRunState**](DagRunState.md) |  | [optional] 
**exception_reason** | **str** |  | [optional] 
**id** | **int** |  | 
**logical_date** | **datetime** |  | [optional] 
**partition_key** | **str** |  | [optional] 
**sort_ordinal** | **int** |  | 

## Example

```python
from airflow_client.client.models.backfill_dag_run_response import BackfillDagRunResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BackfillDagRunResponse from a JSON string
backfill_dag_run_response_instance = BackfillDagRunResponse.from_json(json)
# print the JSON string representation of the object
print(BackfillDagRunResponse.to_json())

# convert the object into a dict
backfill_dag_run_response_dict = backfill_dag_run_response_instance.to_dict()
# create an instance of BackfillDagRunResponse from a dict
backfill_dag_run_response_from_dict = BackfillDagRunResponse.from_dict(backfill_dag_run_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


