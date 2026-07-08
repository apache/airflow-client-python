# BulkDAGRunClearBody

Request body for the bulk clear Dag Runs endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_runs** | [**List[BulkDAGRunBody]**](BulkDAGRunBody.md) |  | [optional] 
**dry_run** | **bool** |  | [optional] [default to True]
**note** | **str** |  | [optional] 
**only_failed** | **bool** |  | [optional] [default to False]
**only_new** | **bool** | Only queue newly added tasks in the latest Dag version without clearing existing tasks. | [optional] [default to False]
**partition_date_end** | **datetime** |  | [optional] 
**partition_date_start** | **datetime** |  | [optional] 
**partition_key** | **str** |  | [optional] 
**run_on_latest_version** | **bool** |  | [optional] 

## Example

```python
from airflow_client.client.models.bulk_dag_run_clear_body import BulkDAGRunClearBody

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDAGRunClearBody from a JSON string
bulk_dag_run_clear_body_instance = BulkDAGRunClearBody.from_json(json)
# print the JSON string representation of the object
print(BulkDAGRunClearBody.to_json())

# convert the object into a dict
bulk_dag_run_clear_body_dict = bulk_dag_run_clear_body_instance.to_dict()
# create an instance of BulkDAGRunClearBody from a dict
bulk_dag_run_clear_body_from_dict = BulkDAGRunClearBody.from_dict(bulk_dag_run_clear_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


