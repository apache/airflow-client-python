# DAGSourceResponse

DAG Source serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 
**dag_id** | **str** |  | 
**version_number** | **int** |  | [optional] 

## Example

```python
from airflow_client.client.models.dag_source_response import DAGSourceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DAGSourceResponse from a JSON string
dag_source_response_instance = DAGSourceResponse.from_json(json)
# print the JSON string representation of the object
print(DAGSourceResponse.to_json())

# convert the object into a dict
dag_source_response_dict = dag_source_response_instance.to_dict()
# create an instance of DAGSourceResponse from a dict
dag_source_response_from_dict = DAGSourceResponse.from_dict(dag_source_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


