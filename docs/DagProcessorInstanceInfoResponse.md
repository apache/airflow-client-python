# DagProcessorInstanceInfoResponse

Dag processor instance info serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bundle_names** | **List[str]** |  | [optional] 
**hostname** | **str** |  | [optional] 
**latest_dag_processor_heartbeat** | **str** |  | [optional] 

## Example

```python
from airflow_client.client.models.dag_processor_instance_info_response import DagProcessorInstanceInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DagProcessorInstanceInfoResponse from a JSON string
dag_processor_instance_info_response_instance = DagProcessorInstanceInfoResponse.from_json(json)
# print the JSON string representation of the object
print(DagProcessorInstanceInfoResponse.to_json())

# convert the object into a dict
dag_processor_instance_info_response_dict = dag_processor_instance_info_response_instance.to_dict()
# create an instance of DagProcessorInstanceInfoResponse from a dict
dag_processor_instance_info_response_from_dict = DagProcessorInstanceInfoResponse.from_dict(dag_processor_instance_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


