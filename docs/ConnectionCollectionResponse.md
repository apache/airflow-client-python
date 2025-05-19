# ConnectionCollectionResponse

Connection Collection serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connections** | [**List[ConnectionResponse]**](ConnectionResponse.md) |  | 
**total_entries** | **int** |  | 

## Example

```python
from airflow_client.client.models.connection_collection_response import ConnectionCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionCollectionResponse from a JSON string
connection_collection_response_instance = ConnectionCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(ConnectionCollectionResponse.to_json())

# convert the object into a dict
connection_collection_response_dict = connection_collection_response_instance.to_dict()
# create an instance of ConnectionCollectionResponse from a dict
connection_collection_response_from_dict = ConnectionCollectionResponse.from_dict(connection_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


