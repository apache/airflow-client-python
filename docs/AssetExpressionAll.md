# AssetExpressionAll

An \"and\" node: ``{\"all\": [...]}`` -- satisfied when all children are satisfied.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all** | [**List[AllInner]**](AllInner.md) |  | 

## Example

```python
from airflow_client.client.models.asset_expression_all import AssetExpressionAll

# TODO update the JSON string below
json = "{}"
# create an instance of AssetExpressionAll from a JSON string
asset_expression_all_instance = AssetExpressionAll.from_json(json)
# print the JSON string representation of the object
print(AssetExpressionAll.to_json())

# convert the object into a dict
asset_expression_all_dict = asset_expression_all_instance.to_dict()
# create an instance of AssetExpressionAll from a dict
asset_expression_all_from_dict = AssetExpressionAll.from_dict(asset_expression_all_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


