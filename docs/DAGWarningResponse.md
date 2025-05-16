# DAGWarningResponse

DAG Warning serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_id** | **str** |  | 
**message** | **str** |  | 
**timestamp** | **datetime** |  | 
**warning_type** | [**DagWarningType**](DagWarningType.md) |  | 

## Example

```python
from airflow_client.client.models.dag_warning_response import DAGWarningResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DAGWarningResponse from a JSON string
dag_warning_response_instance = DAGWarningResponse.from_json(json)
# print the JSON string representation of the object
print(DAGWarningResponse.to_json())

# convert the object into a dict
dag_warning_response_dict = dag_warning_response_instance.to_dict()
# create an instance of DAGWarningResponse from a dict
dag_warning_response_from_dict = DAGWarningResponse.from_dict(dag_warning_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


