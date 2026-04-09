# EntitiesInner1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conn_type** | **str** |  | 
**connection_id** | **str** |  | 
**description** | **str** |  | [optional] 
**extra** | **str** |  | [optional] 
**host** | **str** |  | [optional] 
**login** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**var_schema** | **str** |  | [optional] 
**team_name** | **str** |  | [optional] 

## Example

```python
from airflow_client.client.models.entities_inner1 import EntitiesInner1

# TODO update the JSON string below
json = "{}"
# create an instance of EntitiesInner1 from a JSON string
entities_inner1_instance = EntitiesInner1.from_json(json)
# print the JSON string representation of the object
print(EntitiesInner1.to_json())

# convert the object into a dict
entities_inner1_dict = entities_inner1_instance.to_dict()
# create an instance of EntitiesInner1 from a dict
entities_inner1_from_dict = EntitiesInner1.from_dict(entities_inner1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


