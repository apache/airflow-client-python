# StructuredLogMessage

An individual log message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | **str** |  | 
**timestamp** | **datetime** |  | [optional] 

## Example

```python
from airflow_client.client.models.structured_log_message import StructuredLogMessage

# TODO update the JSON string below
json = "{}"
# create an instance of StructuredLogMessage from a JSON string
structured_log_message_instance = StructuredLogMessage.from_json(json)
# print the JSON string representation of the object
print(StructuredLogMessage.to_json())

# convert the object into a dict
structured_log_message_dict = structured_log_message_instance.to_dict()
# create an instance of StructuredLogMessage from a dict
structured_log_message_from_dict = StructuredLogMessage.from_dict(structured_log_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


