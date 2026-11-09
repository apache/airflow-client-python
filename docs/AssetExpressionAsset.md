# AssetExpressionAsset

An asset leaf: ``{\"asset\": {\"uri\": ..., \"name\": ..., \"group\": ...}}``.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | [**AssetExpressionAssetInfo**](AssetExpressionAssetInfo.md) |  | 

## Example

```python
from airflow_client.client.models.asset_expression_asset import AssetExpressionAsset

# TODO update the JSON string below
json = "{}"
# create an instance of AssetExpressionAsset from a JSON string
asset_expression_asset_instance = AssetExpressionAsset.from_json(json)
# print the JSON string representation of the object
print(AssetExpressionAsset.to_json())

# convert the object into a dict
asset_expression_asset_dict = asset_expression_asset_instance.to_dict()
# create an instance of AssetExpressionAsset from a dict
asset_expression_asset_from_dict = AssetExpressionAsset.from_dict(asset_expression_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


