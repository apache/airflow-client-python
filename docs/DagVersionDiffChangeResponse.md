# DagVersionDiffChangeResponse

One structural difference between two stored Dag versions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after_digest** | **str** |  | [optional] 
**after_value** | **object** | The value this path holds in the target version. Present only when values are disclosed, and omitted entirely when the change has no after side — which is how an absent side is told apart from a stored null. | [optional] 
**before_digest** | **str** |  | [optional] 
**before_value** | **object** | The value this path held in the base version. Present only when values are disclosed, and omitted entirely when the change has no before side — which is how an absent side is told apart from a stored null. | [optional] 
**category** | [**DagVersionDiffCategory**](DagVersionDiffCategory.md) |  | 
**impact** | [**DagVersionDiffImpact**](DagVersionDiffImpact.md) |  | 
**occurrence_count** | **int** | How many underlying changes this record stands for. Always 1 when values are disclosed, since each change is then its own record; a redacted record merges every change sharing its path and operation. | 
**operation** | [**DagVersionDiffOperation**](DagVersionDiffOperation.md) |  | 
**path** | **str** |  | 

## Example

```python
from airflow_client.client.models.dag_version_diff_change_response import DagVersionDiffChangeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DagVersionDiffChangeResponse from a JSON string
dag_version_diff_change_response_instance = DagVersionDiffChangeResponse.from_json(json)
# print the JSON string representation of the object
print(DagVersionDiffChangeResponse.to_json())

# convert the object into a dict
dag_version_diff_change_response_dict = dag_version_diff_change_response_instance.to_dict()
# create an instance of DagVersionDiffChangeResponse from a dict
dag_version_diff_change_response_from_dict = DagVersionDiffChangeResponse.from_dict(dag_version_diff_change_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


