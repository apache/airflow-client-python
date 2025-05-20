# BackfillResponse

Base serializer for Backfill.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | 
**dag_id** | **str** |  | 
**dag_run_conf** | **object** |  | 
**from_date** | **datetime** |  | 
**id** | **int** |  | 
**is_paused** | **bool** |  | 
**max_active_runs** | **int** |  | 
**reprocess_behavior** | [**ReprocessBehavior**](ReprocessBehavior.md) |  | 
**to_date** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from airflow_client.client.models.backfill_response import BackfillResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BackfillResponse from a JSON string
backfill_response_instance = BackfillResponse.from_json(json)
# print the JSON string representation of the object
print(BackfillResponse.to_json())

# convert the object into a dict
backfill_response_dict = backfill_response_instance.to_dict()
# create an instance of BackfillResponse from a dict
backfill_response_from_dict = BackfillResponse.from_dict(backfill_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


