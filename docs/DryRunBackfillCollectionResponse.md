# DryRunBackfillCollectionResponse

Backfill collection serializer for responses in dry-run mode.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backfills** | [**List[DryRunBackfillResponse]**](DryRunBackfillResponse.md) |  | 
**total_entries** | **int** |  | 

## Example

```python
from airflow_client.client.models.dry_run_backfill_collection_response import DryRunBackfillCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DryRunBackfillCollectionResponse from a JSON string
dry_run_backfill_collection_response_instance = DryRunBackfillCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(DryRunBackfillCollectionResponse.to_json())

# convert the object into a dict
dry_run_backfill_collection_response_dict = dry_run_backfill_collection_response_instance.to_dict()
# create an instance of DryRunBackfillCollectionResponse from a dict
dry_run_backfill_collection_response_from_dict = DryRunBackfillCollectionResponse.from_dict(dry_run_backfill_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


