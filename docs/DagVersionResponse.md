# DagVersionResponse

Dag Version serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bundle_name** | **str** |  | [optional] 
**bundle_url** | **str** |  | [optional] 
**bundle_version** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**dag_id** | **str** |  | 
**id** | **str** |  | 
**version_number** | **int** |  | 

## Example

```python
from airflow_client.client.models.dag_version_response import DagVersionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DagVersionResponse from a JSON string
dag_version_response_instance = DagVersionResponse.from_json(json)
# print the JSON string representation of the object
print(DagVersionResponse.to_json())

# convert the object into a dict
dag_version_response_dict = dag_version_response_instance.to_dict()
# create an instance of DagVersionResponse from a dict
dag_version_response_from_dict = DagVersionResponse.from_dict(dag_version_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


