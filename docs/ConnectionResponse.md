# ConnectionResponse

Connection serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **str** |  | 
**conn_type** | **str** |  | 
**description** | **str** |  | 
**host** | **str** |  | 
**login** | **str** |  | 
**var_schema** | **str** |  | 
**port** | **int** |  | 
**password** | **str** |  | 
**extra** | **str** |  | 
**team_name** | **str** |  | 

## Example

```python
from airflow_client.client.models.connection_response import ConnectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionResponse from a JSON string
connection_response_instance = ConnectionResponse.from_json(json)
# print the JSON string representation of the object
print(ConnectionResponse.to_json())

# convert the object into a dict
connection_response_dict = connection_response_instance.to_dict()
# create an instance of ConnectionResponse from a dict
connection_response_from_dict = ConnectionResponse.from_dict(connection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


