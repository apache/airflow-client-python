# DagBundleCollectionResponse

Dag bundle collection response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_bundles** | [**List[DagBundleResponse]**](DagBundleResponse.md) |  | 
**total_entries** | **int** |  | 

## Example

```python
from airflow_client.client.models.dag_bundle_collection_response import DagBundleCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DagBundleCollectionResponse from a JSON string
dag_bundle_collection_response_instance = DagBundleCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(DagBundleCollectionResponse.to_json())

# convert the object into a dict
dag_bundle_collection_response_dict = dag_bundle_collection_response_instance.to_dict()
# create an instance of DagBundleCollectionResponse from a dict
dag_bundle_collection_response_from_dict = DagBundleCollectionResponse.from_dict(dag_bundle_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


