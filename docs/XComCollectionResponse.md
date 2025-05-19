# XComCollectionResponse

XCom Collection serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_entries** | **int** |  | 
**xcom_entries** | [**List[XComResponse]**](XComResponse.md) |  | 

## Example

```python
from airflow_client.client.models.x_com_collection_response import XComCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of XComCollectionResponse from a JSON string
x_com_collection_response_instance = XComCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(XComCollectionResponse.to_json())

# convert the object into a dict
x_com_collection_response_dict = x_com_collection_response_instance.to_dict()
# create an instance of XComCollectionResponse from a dict
x_com_collection_response_from_dict = XComCollectionResponse.from_dict(x_com_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


