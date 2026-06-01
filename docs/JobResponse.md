# JobResponse

Job serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**dag_id** | **str** |  | 
**state** | **str** |  | 
**job_type** | **str** |  | 
**start_date** | **datetime** |  | 
**end_date** | **datetime** |  | 
**latest_heartbeat** | **datetime** |  | 
**executor_class** | **str** |  | 
**hostname** | **str** |  | 
**unixname** | **str** |  | 
**dag_display_name** | **str** |  | [optional] 

## Example

```python
from airflow_client.client.models.job_response import JobResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JobResponse from a JSON string
job_response_instance = JobResponse.from_json(json)
# print the JSON string representation of the object
print(JobResponse.to_json())

# convert the object into a dict
job_response_dict = job_response_instance.to_dict()
# create an instance of JobResponse from a dict
job_response_from_dict = JobResponse.from_dict(job_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


