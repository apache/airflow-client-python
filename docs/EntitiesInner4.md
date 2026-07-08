# EntitiesInner4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**key** | **str** |  | 
**team_name** | **str** |  | [optional] 
**value** | **object** |  | 

## Example

```python
from airflow_client.client.models.entities_inner4 import EntitiesInner4

# TODO update the JSON string below
json = "{}"
# create an instance of EntitiesInner4 from a JSON string
entities_inner4_instance = EntitiesInner4.from_json(json)
# print the JSON string representation of the object
print(EntitiesInner4.to_json())

# convert the object into a dict
entities_inner4_dict = entities_inner4_instance.to_dict()
# create an instance of EntitiesInner4 from a dict
entities_inner4_from_dict = EntitiesInner4.from_dict(entities_inner4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


