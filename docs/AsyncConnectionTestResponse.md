# AsyncConnectionTestResponse

Response returned when polling for the status of an enqueued connection test.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **str** |  | 
**created_at** | **datetime** |  | 
**result_message** | **str** |  | [optional] 
**state** | **str** |  | 
**token** | **str** |  | 

## Example

```python
from airflow_client.client.models.async_connection_test_response import AsyncConnectionTestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncConnectionTestResponse from a JSON string
async_connection_test_response_instance = AsyncConnectionTestResponse.from_json(json)
# print the JSON string representation of the object
print(AsyncConnectionTestResponse.to_json())

# convert the object into a dict
async_connection_test_response_dict = async_connection_test_response_instance.to_dict()
# create an instance of AsyncConnectionTestResponse from a dict
async_connection_test_response_from_dict = AsyncConnectionTestResponse.from_dict(async_connection_test_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


