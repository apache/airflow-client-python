# DagStatsStateResponse

DagStatsState serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**state** | [**DagRunState**](DagRunState.md) |  | 

## Example

```python
from airflow_client.client.models.dag_stats_state_response import DagStatsStateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DagStatsStateResponse from a JSON string
dag_stats_state_response_instance = DagStatsStateResponse.from_json(json)
# print the JSON string representation of the object
print(DagStatsStateResponse.to_json())

# convert the object into a dict
dag_stats_state_response_dict = dag_stats_state_response_instance.to_dict()
# create an instance of DagStatsStateResponse from a dict
dag_stats_state_response_from_dict = DagStatsStateResponse.from_dict(dag_stats_state_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


