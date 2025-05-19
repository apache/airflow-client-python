# DAGRunPatchBody

DAG Run Serializer for PATCH requests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **str** |  | [optional] 
**state** | [**DAGRunPatchStates**](DAGRunPatchStates.md) |  | [optional] 

## Example

```python
from airflow_client.client.models.dag_run_patch_body import DAGRunPatchBody

# TODO update the JSON string below
json = "{}"
# create an instance of DAGRunPatchBody from a JSON string
dag_run_patch_body_instance = DAGRunPatchBody.from_json(json)
# print the JSON string representation of the object
print(DAGRunPatchBody.to_json())

# convert the object into a dict
dag_run_patch_body_dict = dag_run_patch_body_instance.to_dict()
# create an instance of DAGRunPatchBody from a dict
dag_run_patch_body_from_dict = DAGRunPatchBody.from_dict(dag_run_patch_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


