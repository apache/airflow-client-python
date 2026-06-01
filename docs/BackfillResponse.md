# BackfillResponse

Base serializer for Backfill.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**dag_id** | **str** |  | 
**from_date** | **datetime** |  | 
**to_date** | **datetime** |  | 
**dag_run_conf** | **Dict[str, object]** |  | 
**is_paused** | **bool** |  | 
**reprocess_behavior** | [**ReprocessBehavior**](ReprocessBehavior.md) |  | 
**max_active_runs** | **int** |  | 
**created_at** | **datetime** |  | 
**completed_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**dag_display_name** | **str** |  | 

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


