# AssetExpressionAssetInfo

Body of an ``asset`` leaf node.  ``id`` is injected by ``DagModelOperation.update_dag_asset_expression`` when the expression is persisted; ``BaseAsset.as_expression()`` itself only emits ``uri``/``name``/``group``. It is left optional so a row persisted before id-enrichment (or migrated from the pre-3.0 dataset format) degrades gracefully instead of failing response validation.  A leaf the caller is not authorized to read is served with ``hidden`` set and ``uri``, ``name`` and ``id`` blanked (see ``airflow.api_fastapi.common.asset_expression``), so the shape of the schedule stays visible without revealing which asset it waits on.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** |  | 
**hidden** | **bool** |  | [optional] [default to False]
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**uri** | **str** |  | [optional] 

## Example

```python
from airflow_client.client.models.asset_expression_asset_info import AssetExpressionAssetInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AssetExpressionAssetInfo from a JSON string
asset_expression_asset_info_instance = AssetExpressionAssetInfo.from_json(json)
# print the JSON string representation of the object
print(AssetExpressionAssetInfo.to_json())

# convert the object into a dict
asset_expression_asset_info_dict = asset_expression_asset_info_instance.to_dict()
# create an instance of AssetExpressionAssetInfo from a dict
asset_expression_asset_info_from_dict = AssetExpressionAssetInfo.from_dict(asset_expression_asset_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


