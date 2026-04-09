# EntitiesInner2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**include_deferred** | **bool** |  | [optional] [default to False]
**name** | **str** |  | 
**slots** | **int** | Number of slots. Use -1 for unlimited. | 
**team_name** | **str** |  | [optional] 

## Example

```python
from airflow_client.client.models.entities_inner2 import EntitiesInner2

# TODO update the JSON string below
json = "{}"
# create an instance of EntitiesInner2 from a JSON string
entities_inner2_instance = EntitiesInner2.from_json(json)
# print the JSON string representation of the object
print(EntitiesInner2.to_json())

# convert the object into a dict
entities_inner2_dict = entities_inner2_instance.to_dict()
# create an instance of EntitiesInner2 from a dict
entities_inner2_from_dict = EntitiesInner2.from_dict(entities_inner2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


