# AssetExpressionAlias

An asset alias leaf: ``{\"alias\": {\"name\": ..., \"group\": ...}}``.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | [**AssetExpressionAliasInfo**](AssetExpressionAliasInfo.md) |  | 

## Example

```python
from airflow_client.client.models.asset_expression_alias import AssetExpressionAlias

# TODO update the JSON string below
json = "{}"
# create an instance of AssetExpressionAlias from a JSON string
asset_expression_alias_instance = AssetExpressionAlias.from_json(json)
# print the JSON string representation of the object
print(AssetExpressionAlias.to_json())

# convert the object into a dict
asset_expression_alias_dict = asset_expression_alias_instance.to_dict()
# create an instance of AssetExpressionAlias from a dict
asset_expression_alias_from_dict = AssetExpressionAlias.from_dict(asset_expression_alias_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


