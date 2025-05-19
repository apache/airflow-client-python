# DryRunBackfillResponse

Backfill serializer for responses in dry-run mode.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logical_date** | **datetime** |  | 

## Example

```python
from airflow_client.client.models.dry_run_backfill_response import DryRunBackfillResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DryRunBackfillResponse from a JSON string
dry_run_backfill_response_instance = DryRunBackfillResponse.from_json(json)
# print the JSON string representation of the object
print(DryRunBackfillResponse.to_json())

# convert the object into a dict
dry_run_backfill_response_dict = dry_run_backfill_response_instance.to_dict()
# create an instance of DryRunBackfillResponse from a dict
dry_run_backfill_response_from_dict = DryRunBackfillResponse.from_dict(dry_run_backfill_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


