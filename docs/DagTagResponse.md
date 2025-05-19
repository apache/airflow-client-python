# DagTagResponse

DAG Tag serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from airflow_client.client.models.dag_tag_response import DagTagResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DagTagResponse from a JSON string
dag_tag_response_instance = DagTagResponse.from_json(json)
# print the JSON string representation of the object
print(DagTagResponse.to_json())

# convert the object into a dict
dag_tag_response_dict = dag_tag_response_instance.to_dict()
# create an instance of DagTagResponse from a dict
dag_tag_response_from_dict = DagTagResponse.from_dict(dag_tag_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


