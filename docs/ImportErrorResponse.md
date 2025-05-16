# ImportErrorResponse

Import Error Response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bundle_name** | **str** |  | [optional] 
**filename** | **str** |  | 
**import_error_id** | **int** |  | 
**stack_trace** | **str** |  | 
**timestamp** | **datetime** |  | 

## Example

```python
from airflow_client.client.models.import_error_response import ImportErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ImportErrorResponse from a JSON string
import_error_response_instance = ImportErrorResponse.from_json(json)
# print the JSON string representation of the object
print(ImportErrorResponse.to_json())

# convert the object into a dict
import_error_response_dict = import_error_response_instance.to_dict()
# create an instance of ImportErrorResponse from a dict
import_error_response_from_dict = ImportErrorResponse.from_dict(import_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


