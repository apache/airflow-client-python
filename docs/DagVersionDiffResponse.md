# DagVersionDiffResponse

Observed-state difference between two stored Dag versions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_version_number** | **int** |  | 
**changes** | [**List[DagVersionDiffChangeResponse]**](DagVersionDiffChangeResponse.md) |  | 
**diff_schema_version** | **int** | Wire format of this payload. Incremented when its shape changes. | 
**mode** | [**DagVersionDiffMode**](DagVersionDiffMode.md) |  | 
**serializer_versions** | [**DagVersionDiffSerializerVersions**](DagVersionDiffSerializerVersions.md) |  | 
**target_version_number** | **int** |  | 
**total_changes** | **int** | Underlying changes across every disclosed path, not the number of records. Exact when &#x60;truncated&#x60; is false; a lower bound when it is true, because the changes at dropped paths are not counted. | 
**truncated** | **bool** | Whether a change at a path not already in &#x60;changes&#x60; was dropped to stay within &#x60;max_changes&#x60;. Paths that are absent are absent, not unchanged. | 
**unavailable_reason** | **str** |  | [optional] 
**values_status** | [**DagVersionDiffValuesStatus**](DagVersionDiffValuesStatus.md) |  | 

## Example

```python
from airflow_client.client.models.dag_version_diff_response import DagVersionDiffResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DagVersionDiffResponse from a JSON string
dag_version_diff_response_instance = DagVersionDiffResponse.from_json(json)
# print the JSON string representation of the object
print(DagVersionDiffResponse.to_json())

# convert the object into a dict
dag_version_diff_response_dict = dag_version_diff_response_instance.to_dict()
# create an instance of DagVersionDiffResponse from a dict
dag_version_diff_response_from_dict = DagVersionDiffResponse.from_dict(dag_version_diff_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


