# AssetExpressionAliasInfo

Body of an ``alias`` leaf node.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from airflow_client.client.models.asset_expression_alias_info import AssetExpressionAliasInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AssetExpressionAliasInfo from a JSON string
asset_expression_alias_info_instance = AssetExpressionAliasInfo.from_json(json)
# print the JSON string representation of the object
print(AssetExpressionAliasInfo.to_json())

# convert the object into a dict
asset_expression_alias_info_dict = asset_expression_alias_info_instance.to_dict()
# create an instance of AssetExpressionAliasInfo from a dict
asset_expression_alias_info_from_dict = AssetExpressionAliasInfo.from_dict(asset_expression_alias_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


