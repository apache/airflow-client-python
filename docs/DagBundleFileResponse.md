# DagBundleFileResponse

A file in a Dag bundle, as the Dag processor last saw it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_count** | **int** | Number of live Dags the file defines that the caller may read. | 
**import_error_count** | **int** |  | [optional] 
**last_parse_duration** | **float** |  | [optional] 
**last_parsed_time** | **datetime** |  | [optional] 
**relative_fileloc** | **str** |  | 

## Example

```python
from airflow_client.client.models.dag_bundle_file_response import DagBundleFileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DagBundleFileResponse from a JSON string
dag_bundle_file_response_instance = DagBundleFileResponse.from_json(json)
# print the JSON string representation of the object
print(DagBundleFileResponse.to_json())

# convert the object into a dict
dag_bundle_file_response_dict = dag_bundle_file_response_instance.to_dict()
# create an instance of DagBundleFileResponse from a dict
dag_bundle_file_response_from_dict = DagBundleFileResponse.from_dict(dag_bundle_file_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


