# HITLDetailCollection

Schema for a collection of Human-in-the-loop details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hitl_details** | [**List[HITLDetail]**](HITLDetail.md) |  | 
**total_entries** | **int** |  | 

## Example

```python
from airflow_client.client.models.hitl_detail_collection import HITLDetailCollection

# TODO update the JSON string below
json = "{}"
# create an instance of HITLDetailCollection from a JSON string
hitl_detail_collection_instance = HITLDetailCollection.from_json(json)
# print the JSON string representation of the object
print(HITLDetailCollection.to_json())

# convert the object into a dict
hitl_detail_collection_dict = hitl_detail_collection_instance.to_dict()
# create an instance of HITLDetailCollection from a dict
hitl_detail_collection_from_dict = HITLDetailCollection.from_dict(hitl_detail_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


