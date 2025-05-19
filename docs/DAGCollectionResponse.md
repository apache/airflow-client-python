# DAGCollectionResponse

DAG Collection serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dags** | [**List[DAGResponse]**](DAGResponse.md) |  | 
**total_entries** | **int** |  | 

## Example

```python
from airflow_client.client.models.dag_collection_response import DAGCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DAGCollectionResponse from a JSON string
dag_collection_response_instance = DAGCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(DAGCollectionResponse.to_json())

# convert the object into a dict
dag_collection_response_dict = dag_collection_response_instance.to_dict()
# create an instance of DAGCollectionResponse from a dict
dag_collection_response_from_dict = DAGCollectionResponse.from_dict(dag_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


