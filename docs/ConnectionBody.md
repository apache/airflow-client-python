# ConnectionBody

Connection Serializer for requests body.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conn_type** | **str** |  | 
**connection_id** | **str** |  | 
**description** | **str** |  | [optional] 
**extra** | **str** |  | [optional] 
**host** | **str** |  | [optional] 
**login** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**var_schema** | **str** |  | [optional] 

## Example

```python
from airflow_client.client.models.connection_body import ConnectionBody

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionBody from a JSON string
connection_body_instance = ConnectionBody.from_json(json)
# print the JSON string representation of the object
print(ConnectionBody.to_json())

# convert the object into a dict
connection_body_dict = connection_body_instance.to_dict()
# create an instance of ConnectionBody from a dict
connection_body_from_dict = ConnectionBody.from_dict(connection_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


