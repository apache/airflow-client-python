# BaseInfoResponse

Base info serializer for responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 

## Example

```python
from airflow_client.client.models.base_info_response import BaseInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BaseInfoResponse from a JSON string
base_info_response_instance = BaseInfoResponse.from_json(json)
# print the JSON string representation of the object
print(BaseInfoResponse.to_json())

# convert the object into a dict
base_info_response_dict = base_info_response_instance.to_dict()
# create an instance of BaseInfoResponse from a dict
base_info_response_from_dict = BaseInfoResponse.from_dict(base_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


