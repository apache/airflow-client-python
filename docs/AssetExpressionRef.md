# AssetExpressionRef

An unresolved asset reference leaf: ``{\"asset_ref\": {\"name\": ...}}`` or ``{\"asset_ref\": {\"uri\": ...}}``.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_ref** | **Dict[str, str]** |  | 

## Example

```python
from airflow_client.client.models.asset_expression_ref import AssetExpressionRef

# TODO update the JSON string below
json = "{}"
# create an instance of AssetExpressionRef from a JSON string
asset_expression_ref_instance = AssetExpressionRef.from_json(json)
# print the JSON string representation of the object
print(AssetExpressionRef.to_json())

# convert the object into a dict
asset_expression_ref_dict = asset_expression_ref_instance.to_dict()
# create an instance of AssetExpressionRef from a dict
asset_expression_ref_from_dict = AssetExpressionRef.from_dict(asset_expression_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


