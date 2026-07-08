# ClearPartitionsBody

Request body for the clearPartitions endpoint (column-reset: set partition fields to None).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clear_task_instances** | **bool** | Also clear task instances on the matched runs. | [optional] [default to False]
**dry_run** | **bool** | If True, compute counts without writing any changes. | [optional] [default to True]
**partition_date_end** | **datetime** |  | [optional] 
**partition_date_start** | **datetime** |  | [optional] 
**partition_key** | **str** |  | [optional] 
**run_id** | **str** |  | [optional] 

## Example

```python
from airflow_client.client.models.clear_partitions_body import ClearPartitionsBody

# TODO update the JSON string below
json = "{}"
# create an instance of ClearPartitionsBody from a JSON string
clear_partitions_body_instance = ClearPartitionsBody.from_json(json)
# print the JSON string representation of the object
print(ClearPartitionsBody.to_json())

# convert the object into a dict
clear_partitions_body_dict = clear_partitions_body_instance.to_dict()
# create an instance of ClearPartitionsBody from a dict
clear_partitions_body_from_dict = ClearPartitionsBody.from_dict(clear_partitions_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


