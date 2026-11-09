# AssetExpressionAny

An \"or\" node: ``{\"any\": [...]}`` -- satisfied when any child is satisfied.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**any** | [**List[AllInner]**](AllInner.md) |  | 

## Example

```python
from airflow_client.client.models.asset_expression_any import AssetExpressionAny

# TODO update the JSON string below
json = "{}"
# create an instance of AssetExpressionAny from a JSON string
asset_expression_any_instance = AssetExpressionAny.from_json(json)
# print the JSON string representation of the object
print(AssetExpressionAny.to_json())

# convert the object into a dict
asset_expression_any_dict = asset_expression_any_instance.to_dict()
# create an instance of AssetExpressionAny from a dict
asset_expression_any_from_dict = AssetExpressionAny.from_dict(asset_expression_any_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


