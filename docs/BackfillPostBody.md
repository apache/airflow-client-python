# BackfillPostBody

Object used for create backfill request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_id** | **str** |  | 
**dag_run_conf** | **object** |  | [optional] 
**from_date** | **datetime** |  | 
**max_active_runs** | **int** |  | [optional] [default to 10]
**reprocess_behavior** | [**ReprocessBehavior**](ReprocessBehavior.md) |  | [optional] 
**run_backwards** | **bool** |  | [optional] [default to False]
**to_date** | **datetime** |  | 

## Example

```python
from airflow_client.client.models.backfill_post_body import BackfillPostBody

# TODO update the JSON string below
json = "{}"
# create an instance of BackfillPostBody from a JSON string
backfill_post_body_instance = BackfillPostBody.from_json(json)
# print the JSON string representation of the object
print(BackfillPostBody.to_json())

# convert the object into a dict
backfill_post_body_dict = backfill_post_body_instance.to_dict()
# create an instance of BackfillPostBody from a dict
backfill_post_body_from_dict = BackfillPostBody.from_dict(backfill_post_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


