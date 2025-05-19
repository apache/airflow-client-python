# DAGTagCollectionResponse

DAG Tags Collection serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | **List[str]** |  | 
**total_entries** | **int** |  | 

## Example

```python
from airflow_client.client.models.dag_tag_collection_response import DAGTagCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DAGTagCollectionResponse from a JSON string
dag_tag_collection_response_instance = DAGTagCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(DAGTagCollectionResponse.to_json())

# convert the object into a dict
dag_tag_collection_response_dict = dag_tag_collection_response_instance.to_dict()
# create an instance of DAGTagCollectionResponse from a dict
dag_tag_collection_response_from_dict = DAGTagCollectionResponse.from_dict(dag_tag_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


