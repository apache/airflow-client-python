# DAGWarningCollectionResponse

DAG warning collection serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_warnings** | [**List[DAGWarningResponse]**](DAGWarningResponse.md) |  | 
**total_entries** | **int** |  | 

## Example

```python
from airflow_client.client.models.dag_warning_collection_response import DAGWarningCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DAGWarningCollectionResponse from a JSON string
dag_warning_collection_response_instance = DAGWarningCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(DAGWarningCollectionResponse.to_json())

# convert the object into a dict
dag_warning_collection_response_dict = dag_warning_collection_response_instance.to_dict()
# create an instance of DAGWarningCollectionResponse from a dict
dag_warning_collection_response_from_dict = DAGWarningCollectionResponse.from_dict(dag_warning_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


