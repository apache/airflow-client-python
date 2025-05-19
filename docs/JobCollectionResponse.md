# JobCollectionResponse

Job Collection Response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobs** | [**List[JobResponse]**](JobResponse.md) |  | 
**total_entries** | **int** |  | 

## Example

```python
from airflow_client.client.models.job_collection_response import JobCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JobCollectionResponse from a JSON string
job_collection_response_instance = JobCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(JobCollectionResponse.to_json())

# convert the object into a dict
job_collection_response_dict = job_collection_response_instance.to_dict()
# create an instance of JobCollectionResponse from a dict
job_collection_response_from_dict = JobCollectionResponse.from_dict(job_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


