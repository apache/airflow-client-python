# EntitiesInner3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**key** | **str** |  | 
**team_name** | **str** |  | [optional] 
**value** | **object** |  | 

## Example

```python
from airflow_client.client.models.entities_inner3 import EntitiesInner3

# TODO update the JSON string below
json = "{}"
# create an instance of EntitiesInner3 from a JSON string
entities_inner3_instance = EntitiesInner3.from_json(json)
# print the JSON string representation of the object
print(EntitiesInner3.to_json())

# convert the object into a dict
entities_inner3_dict = entities_inner3_instance.to_dict()
# create an instance of EntitiesInner3 from a dict
entities_inner3_from_dict = EntitiesInner3.from_dict(entities_inner3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


