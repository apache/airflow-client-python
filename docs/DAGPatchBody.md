# DAGPatchBody

Dag Serializer for updatable bodies.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_paused** | **bool** |  | 

## Example

```python
from airflow_client.client.models.dag_patch_body import DAGPatchBody

# TODO update the JSON string below
json = "{}"
# create an instance of DAGPatchBody from a JSON string
dag_patch_body_instance = DAGPatchBody.from_json(json)
# print the JSON string representation of the object
print(DAGPatchBody.to_json())

# convert the object into a dict
dag_patch_body_dict = dag_patch_body_instance.to_dict()
# create an instance of DAGPatchBody from a dict
dag_patch_body_from_dict = DAGPatchBody.from_dict(dag_patch_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


