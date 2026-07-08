# EntitiesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_id** | **str** |  | [optional] 
**dag_run_id** | **str** |  | 
**note** | **str** |  | [optional] 
**state** | [**DagRunMutableStates**](DagRunMutableStates.md) |  | [optional] 

## Example

```python
from airflow_client.client.models.entities_inner import EntitiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of EntitiesInner from a JSON string
entities_inner_instance = EntitiesInner.from_json(json)
# print the JSON string representation of the object
print(EntitiesInner.to_json())

# convert the object into a dict
entities_inner_dict = entities_inner_instance.to_dict()
# create an instance of EntitiesInner from a dict
entities_inner_from_dict = EntitiesInner.from_dict(entities_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


