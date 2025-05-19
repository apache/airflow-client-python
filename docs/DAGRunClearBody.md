# DAGRunClearBody

DAG Run serializer for clear endpoint body.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **bool** |  | [optional] [default to True]
**only_failed** | **bool** |  | [optional] [default to False]

## Example

```python
from airflow_client.client.models.dag_run_clear_body import DAGRunClearBody

# TODO update the JSON string below
json = "{}"
# create an instance of DAGRunClearBody from a JSON string
dag_run_clear_body_instance = DAGRunClearBody.from_json(json)
# print the JSON string representation of the object
print(DAGRunClearBody.to_json())

# convert the object into a dict
dag_run_clear_body_dict = dag_run_clear_body_instance.to_dict()
# create an instance of DAGRunClearBody from a dict
dag_run_clear_body_from_dict = DAGRunClearBody.from_dict(dag_run_clear_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


