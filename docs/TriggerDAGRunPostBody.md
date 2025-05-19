# TriggerDAGRunPostBody

Trigger DAG Run Serializer for POST body.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conf** | **object** |  | [optional] 
**dag_run_id** | **str** |  | [optional] 
**data_interval_end** | **datetime** |  | [optional] 
**data_interval_start** | **datetime** |  | [optional] 
**logical_date** | **datetime** |  | [optional] 
**note** | **str** |  | [optional] 
**run_after** | **datetime** |  | [optional] 

## Example

```python
from airflow_client.client.models.trigger_dag_run_post_body import TriggerDAGRunPostBody

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerDAGRunPostBody from a JSON string
trigger_dag_run_post_body_instance = TriggerDAGRunPostBody.from_json(json)
# print the JSON string representation of the object
print(TriggerDAGRunPostBody.to_json())

# convert the object into a dict
trigger_dag_run_post_body_dict = trigger_dag_run_post_body_instance.to_dict()
# create an instance of TriggerDAGRunPostBody from a dict
trigger_dag_run_post_body_from_dict = TriggerDAGRunPostBody.from_dict(trigger_dag_run_post_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


