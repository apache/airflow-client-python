# ClearPartitionsResponse

Response for the clearPartitions endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_runs_cleared** | **int** |  | 
**dry_run** | **bool** |  | 
**task_instances_cleared** | **int** |  | 

## Example

```python
from airflow_client.client.models.clear_partitions_response import ClearPartitionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClearPartitionsResponse from a JSON string
clear_partitions_response_instance = ClearPartitionsResponse.from_json(json)
# print the JSON string representation of the object
print(ClearPartitionsResponse.to_json())

# convert the object into a dict
clear_partitions_response_dict = clear_partitions_response_instance.to_dict()
# create an instance of ClearPartitionsResponse from a dict
clear_partitions_response_from_dict = ClearPartitionsResponse.from_dict(clear_partitions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


