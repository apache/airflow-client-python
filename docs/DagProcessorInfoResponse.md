# DagProcessorInfoResponse

DagProcessor info serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latest_dag_processor_heartbeat** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from airflow_client.client.models.dag_processor_info_response import DagProcessorInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DagProcessorInfoResponse from a JSON string
dag_processor_info_response_instance = DagProcessorInfoResponse.from_json(json)
# print the JSON string representation of the object
print(DagProcessorInfoResponse.to_json())

# convert the object into a dict
dag_processor_info_response_dict = dag_processor_info_response_instance.to_dict()
# create an instance of DagProcessorInfoResponse from a dict
dag_processor_info_response_from_dict = DagProcessorInfoResponse.from_dict(dag_processor_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


