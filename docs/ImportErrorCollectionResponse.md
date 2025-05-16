# ImportErrorCollectionResponse

Import Error Collection Response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**import_errors** | [**List[ImportErrorResponse]**](ImportErrorResponse.md) |  | 
**total_entries** | **int** |  | 

## Example

```python
from airflow_client.client.models.import_error_collection_response import ImportErrorCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ImportErrorCollectionResponse from a JSON string
import_error_collection_response_instance = ImportErrorCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(ImportErrorCollectionResponse.to_json())

# convert the object into a dict
import_error_collection_response_dict = import_error_collection_response_instance.to_dict()
# create an instance of ImportErrorCollectionResponse from a dict
import_error_collection_response_from_dict = ImportErrorCollectionResponse.from_dict(import_error_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


