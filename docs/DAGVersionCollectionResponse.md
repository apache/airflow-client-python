# DAGVersionCollectionResponse

DAG Version Collection serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_versions** | [**List[DagVersionResponse]**](DagVersionResponse.md) |  | 
**total_entries** | **int** |  | 

## Example

```python
from airflow_client.client.models.dag_version_collection_response import DAGVersionCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DAGVersionCollectionResponse from a JSON string
dag_version_collection_response_instance = DAGVersionCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(DAGVersionCollectionResponse.to_json())

# convert the object into a dict
dag_version_collection_response_dict = dag_version_collection_response_instance.to_dict()
# create an instance of DAGVersionCollectionResponse from a dict
dag_version_collection_response_from_dict = DAGVersionCollectionResponse.from_dict(dag_version_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


