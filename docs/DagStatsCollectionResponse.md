# DagStatsCollectionResponse

DAG Stats Collection serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dags** | [**List[DagStatsResponse]**](DagStatsResponse.md) |  | 
**total_entries** | **int** |  | 

## Example

```python
from airflow_client.client.models.dag_stats_collection_response import DagStatsCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DagStatsCollectionResponse from a JSON string
dag_stats_collection_response_instance = DagStatsCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(DagStatsCollectionResponse.to_json())

# convert the object into a dict
dag_stats_collection_response_dict = dag_stats_collection_response_instance.to_dict()
# create an instance of DagStatsCollectionResponse from a dict
dag_stats_collection_response_from_dict = DagStatsCollectionResponse.from_dict(dag_stats_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


