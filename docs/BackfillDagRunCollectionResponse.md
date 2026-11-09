# BackfillDagRunCollectionResponse

BackfillDagRun Collection serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backfill_dag_runs** | [**List[BackfillDagRunResponse]**](BackfillDagRunResponse.md) |  | 
**total_entries** | **int** |  | 

## Example

```python
from airflow_client.client.models.backfill_dag_run_collection_response import BackfillDagRunCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BackfillDagRunCollectionResponse from a JSON string
backfill_dag_run_collection_response_instance = BackfillDagRunCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(BackfillDagRunCollectionResponse.to_json())

# convert the object into a dict
backfill_dag_run_collection_response_dict = backfill_dag_run_collection_response_instance.to_dict()
# create an instance of BackfillDagRunCollectionResponse from a dict
backfill_dag_run_collection_response_from_dict = BackfillDagRunCollectionResponse.from_dict(backfill_dag_run_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


