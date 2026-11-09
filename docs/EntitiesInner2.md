# EntitiesInner2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_id** | **str** |  | [optional] 
**dag_run_id** | **str** |  | [optional] 
**include_downstream** | **bool** |  | [optional] [default to False]
**include_future** | **bool** |  | [optional] [default to False]
**include_past** | **bool** |  | [optional] [default to False]
**include_upstream** | **bool** |  | [optional] [default to False]
**map_index** | **int** |  | [optional] 
**new_state** | [**TaskInstanceState**](TaskInstanceState.md) |  | [optional] 
**note** | **str** |  | [optional] 
**region_id** | **UUID** |  | [optional] 
**region_index** | **int** |  | [optional] 
**task_id** | **str** |  | 

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


