# BackfillCollectionResponse

Backfill Collection serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backfills** | [**List[BackfillResponse]**](BackfillResponse.md) |  | 
**total_entries** | **int** |  | 

## Example

```python
from airflow_client.client.models.backfill_collection_response import BackfillCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BackfillCollectionResponse from a JSON string
backfill_collection_response_instance = BackfillCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(BackfillCollectionResponse.to_json())

# convert the object into a dict
backfill_collection_response_dict = backfill_collection_response_instance.to_dict()
# create an instance of BackfillCollectionResponse from a dict
backfill_collection_response_from_dict = BackfillCollectionResponse.from_dict(backfill_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


