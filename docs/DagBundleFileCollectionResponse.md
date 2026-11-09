# DagBundleFileCollectionResponse

Dag bundle file collection response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_bundle_files** | [**List[DagBundleFileResponse]**](DagBundleFileResponse.md) |  | 
**total_entries** | **int** |  | 

## Example

```python
from airflow_client.client.models.dag_bundle_file_collection_response import DagBundleFileCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DagBundleFileCollectionResponse from a JSON string
dag_bundle_file_collection_response_instance = DagBundleFileCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(DagBundleFileCollectionResponse.to_json())

# convert the object into a dict
dag_bundle_file_collection_response_dict = dag_bundle_file_collection_response_instance.to_dict()
# create an instance of DagBundleFileCollectionResponse from a dict
dag_bundle_file_collection_response_from_dict = DagBundleFileCollectionResponse.from_dict(dag_bundle_file_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


