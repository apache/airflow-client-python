# DagBundleDetailResponse

Dag bundle serializer for the single-bundle response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**bundle_url** | **str** |  | [optional] 
**dag_count** | **int** | Number of live Dags recorded against the bundle that the caller is permitted to see, counted on the same terms as &#x60;&#x60;GET /dags&#x60;&#x60;. | 
**import_error_count** | **int** |  | [optional] 
**last_refreshed** | **datetime** |  | [optional] 
**name** | **str** |  | 
**team_name** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from airflow_client.client.models.dag_bundle_detail_response import DagBundleDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DagBundleDetailResponse from a JSON string
dag_bundle_detail_response_instance = DagBundleDetailResponse.from_json(json)
# print the JSON string representation of the object
print(DagBundleDetailResponse.to_json())

# convert the object into a dict
dag_bundle_detail_response_dict = dag_bundle_detail_response_instance.to_dict()
# create an instance of DagBundleDetailResponse from a dict
dag_bundle_detail_response_from_dict = DagBundleDetailResponse.from_dict(dag_bundle_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


