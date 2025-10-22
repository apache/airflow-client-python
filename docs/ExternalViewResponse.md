# ExternalViewResponse

Serializer for External View Plugin responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [optional] 
**destination** | **str** |  | [optional] [default to 'nav']
**href** | **str** |  | 
**icon** | **str** |  | [optional] 
**icon_dark_mode** | **str** |  | [optional] 
**name** | **str** |  | 
**url_route** | **str** |  | [optional] 

## Example

```python
from airflow_client.client.models.external_view_response import ExternalViewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalViewResponse from a JSON string
external_view_response_instance = ExternalViewResponse.from_json(json)
# print the JSON string representation of the object
print(ExternalViewResponse.to_json())

# convert the object into a dict
external_view_response_dict = external_view_response_instance.to_dict()
# create an instance of ExternalViewResponse from a dict
external_view_response_from_dict = ExternalViewResponse.from_dict(external_view_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


