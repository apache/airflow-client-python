# EntitiesInner5


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**key** | **str** |  | 
**team_name** | **str** |  | [optional] 
**value** | **object** |  | 

## Example

```python
from airflow_client.client.models.entities_inner5 import EntitiesInner5

# TODO update the JSON string below
json = "{}"
# create an instance of EntitiesInner5 from a JSON string
entities_inner5_instance = EntitiesInner5.from_json(json)
# print the JSON string representation of the object
print(EntitiesInner5.to_json())

# convert the object into a dict
entities_inner5_dict = entities_inner5_instance.to_dict()
# create an instance of EntitiesInner5 from a dict
entities_inner5_from_dict = EntitiesInner5.from_dict(entities_inner5_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


