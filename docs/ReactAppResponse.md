# ReactAppResponse

Serializer for React App Plugin responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bundle_url** | **str** |  | 
**category** | **str** |  | [optional] 
**destination** | **str** |  | [optional] [default to 'nav']
**icon** | **str** |  | [optional] 
**icon_dark_mode** | **str** |  | [optional] 
**name** | **str** |  | 
**url_route** | **str** |  | [optional] 

## Example

```python
from airflow_client.client.models.react_app_response import ReactAppResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReactAppResponse from a JSON string
react_app_response_instance = ReactAppResponse.from_json(json)
# print the JSON string representation of the object
print(ReactAppResponse.to_json())

# convert the object into a dict
react_app_response_dict = react_app_response_instance.to_dict()
# create an instance of ReactAppResponse from a dict
react_app_response_from_dict = ReactAppResponse.from_dict(react_app_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


