# MaterializeAssetBody

Materialize asset request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conf** | **Dict[str, object]** |  | [optional] 
**dag_run_id** | **str** |  | [optional] 
**data_interval_end** | **datetime** |  | [optional] 
**data_interval_start** | **datetime** |  | [optional] 
**logical_date** | **datetime** |  | [optional] 
**note** | **str** |  | [optional] 
**partition_key** | **str** |  | [optional] 
**run_after** | **datetime** |  | [optional] 

## Example

```python
from airflow_client.client.models.materialize_asset_body import MaterializeAssetBody

# TODO update the JSON string below
json = "{}"
# create an instance of MaterializeAssetBody from a JSON string
materialize_asset_body_instance = MaterializeAssetBody.from_json(json)
# print the JSON string representation of the object
print(MaterializeAssetBody.to_json())

# convert the object into a dict
materialize_asset_body_dict = materialize_asset_body_instance.to_dict()
# create an instance of MaterializeAssetBody from a dict
materialize_asset_body_from_dict = MaterializeAssetBody.from_dict(materialize_asset_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


