# DAGRunCollectionResponse

DAG Run Collection serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_runs** | [**List[DAGRunResponse]**](DAGRunResponse.md) |  | 
**total_entries** | **int** |  | 

## Example

```python
from airflow_client.client.models.dag_run_collection_response import DAGRunCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DAGRunCollectionResponse from a JSON string
dag_run_collection_response_instance = DAGRunCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(DAGRunCollectionResponse.to_json())

# convert the object into a dict
dag_run_collection_response_dict = dag_run_collection_response_instance.to_dict()
# create an instance of DAGRunCollectionResponse from a dict
dag_run_collection_response_from_dict = DAGRunCollectionResponse.from_dict(dag_run_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


