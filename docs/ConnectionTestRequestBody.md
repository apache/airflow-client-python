# ConnectionTestRequestBody

Request body for enqueueing a connection test on a worker.  Inherits ``connection_id`` pattern, ``extra`` JSON validation, and ``team_name`` handling from ``ConnectionBody`` so tested connections share the same input contract as persisted ones.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit_on_success** | **bool** | If True, save or update the connection in the connection table when the test succeeds. | [optional] [default to False]
**conn_type** | **str** |  | 
**connection_id** | **str** |  | 
**description** | **str** |  | [optional] 
**executor** | **str** |  | [optional] 
**extra** | **str** |  | [optional] 
**host** | **str** |  | [optional] 
**login** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**queue** | **str** |  | [optional] 
**var_schema** | **str** |  | [optional] 
**team_name** | **str** |  | [optional] 

## Example

```python
from airflow_client.client.models.connection_test_request_body import ConnectionTestRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionTestRequestBody from a JSON string
connection_test_request_body_instance = ConnectionTestRequestBody.from_json(json)
# print the JSON string representation of the object
print(ConnectionTestRequestBody.to_json())

# convert the object into a dict
connection_test_request_body_dict = connection_test_request_body_instance.to_dict()
# create an instance of ConnectionTestRequestBody from a dict
connection_test_request_body_from_dict = ConnectionTestRequestBody.from_dict(connection_test_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


