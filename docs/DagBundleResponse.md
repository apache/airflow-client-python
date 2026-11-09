# DagBundleResponse

Dag bundle serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**bundle_url** | **str** |  | [optional] 
**import_error_count** | **int** |  | [optional] 
**last_refreshed** | **datetime** |  | [optional] 
**name** | **str** |  | 
**team_name** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from airflow_client.client.models.dag_bundle_response import DagBundleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DagBundleResponse from a JSON string
dag_bundle_response_instance = DagBundleResponse.from_json(json)
# print the JSON string representation of the object
print(DagBundleResponse.to_json())

# convert the object into a dict
dag_bundle_response_dict = dag_bundle_response_instance.to_dict()
# create an instance of DagBundleResponse from a dict
dag_bundle_response_from_dict = DagBundleResponse.from_dict(dag_bundle_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


