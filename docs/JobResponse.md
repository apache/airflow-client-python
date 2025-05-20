# JobResponse

Job serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_id** | **str** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**executor_class** | **str** |  | [optional] 
**hostname** | **str** |  | [optional] 
**id** | **int** |  | 
**job_type** | **str** |  | [optional] 
**latest_heartbeat** | **datetime** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**state** | **str** |  | [optional] 
**unixname** | **str** |  | [optional] 

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


