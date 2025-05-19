# ExternalLogUrlResponse

Response for the external log URL endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 

## Example

```python
from airflow_client.client.models.external_log_url_response import ExternalLogUrlResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalLogUrlResponse from a JSON string
external_log_url_response_instance = ExternalLogUrlResponse.from_json(json)
# print the JSON string representation of the object
print(ExternalLogUrlResponse.to_json())

# convert the object into a dict
external_log_url_response_dict = external_log_url_response_instance.to_dict()
# create an instance of ExternalLogUrlResponse from a dict
external_log_url_response_from_dict = ExternalLogUrlResponse.from_dict(external_log_url_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


