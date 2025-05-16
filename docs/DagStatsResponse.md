# DagStatsResponse

DAG Stats serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_id** | **str** |  | 
**stats** | [**List[DagStatsStateResponse]**](DagStatsStateResponse.md) |  | 

## Example

```python
from airflow_client.client.models.dag_stats_response import DagStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DagStatsResponse from a JSON string
dag_stats_response_instance = DagStatsResponse.from_json(json)
# print the JSON string representation of the object
print(DagStatsResponse.to_json())

# convert the object into a dict
dag_stats_response_dict = dag_stats_response_instance.to_dict()
# create an instance of DagStatsResponse from a dict
dag_stats_response_from_dict = DagStatsResponse.from_dict(dag_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


