# AllInner


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
from airflow_client.client.models.all_inner import AllInner

# TODO update the JSON string below
json = "{}"
# create an instance of AllInner from a JSON string
all_inner_instance = AllInner.from_json(json)
# print the JSON string representation of the object
print(AllInner.to_json())

# convert the object into a dict
all_inner_dict = all_inner_instance.to_dict()
# create an instance of AllInner from a dict
all_inner_from_dict = AllInner.from_dict(all_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


