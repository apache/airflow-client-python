# DAGDetailsResponseAssetExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | [**AssetExpressionAssetInfo**](AssetExpressionAssetInfo.md) |  | 
**alias** | [**AssetExpressionAliasInfo**](AssetExpressionAliasInfo.md) |  | 
**asset_ref** | **Dict[str, str]** |  | 
**any** | [**List[AllInner]**](AllInner.md) |  | 
**all** | [**List[AllInner]**](AllInner.md) |  | 

## Example

```python
from airflow_client.client.models.dag_details_response_asset_expression import DAGDetailsResponseAssetExpression

# TODO update the JSON string below
json = "{}"
# create an instance of DAGDetailsResponseAssetExpression from a JSON string
dag_details_response_asset_expression_instance = DAGDetailsResponseAssetExpression.from_json(json)
# print the JSON string representation of the object
print(DAGDetailsResponseAssetExpression.to_json())

# convert the object into a dict
dag_details_response_asset_expression_dict = dag_details_response_asset_expression_instance.to_dict()
# create an instance of DAGDetailsResponseAssetExpression from a dict
dag_details_response_asset_expression_from_dict = DAGDetailsResponseAssetExpression.from_dict(dag_details_response_asset_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


