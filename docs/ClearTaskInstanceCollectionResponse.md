# ClearTaskInstanceCollectionResponse

Response for clear dag run dry run, which may contain new tasks without full TaskInstance data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_instances** | [**List[TaskInstancesInner]**](TaskInstancesInner.md) |  | 
**total_entries** | **int** |  | 

## Example

```python
from airflow_client.client.models.clear_task_instance_collection_response import ClearTaskInstanceCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClearTaskInstanceCollectionResponse from a JSON string
clear_task_instance_collection_response_instance = ClearTaskInstanceCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(ClearTaskInstanceCollectionResponse.to_json())

# convert the object into a dict
clear_task_instance_collection_response_dict = clear_task_instance_collection_response_instance.to_dict()
# create an instance of ClearTaskInstanceCollectionResponse from a dict
clear_task_instance_collection_response_from_dict = ClearTaskInstanceCollectionResponse.from_dict(clear_task_instance_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


