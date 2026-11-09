# DagVersionDiffSerializerVersions

Which Dag serializer format each compared version was stored under.  Unrelated to ``diff_schema_version``, which versions this payload rather than the serialized Dags it describes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | **int** |  | [optional] 
**target** | **int** |  | [optional] 

## Example

```python
from airflow_client.client.models.dag_version_diff_serializer_versions import DagVersionDiffSerializerVersions

# TODO update the JSON string below
json = "{}"
# create an instance of DagVersionDiffSerializerVersions from a JSON string
dag_version_diff_serializer_versions_instance = DagVersionDiffSerializerVersions.from_json(json)
# print the JSON string representation of the object
print(DagVersionDiffSerializerVersions.to_json())

# convert the object into a dict
dag_version_diff_serializer_versions_dict = dag_version_diff_serializer_versions_instance.to_dict()
# create an instance of DagVersionDiffSerializerVersions from a dict
dag_version_diff_serializer_versions_from_dict = DagVersionDiffSerializerVersions.from_dict(dag_version_diff_serializer_versions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


