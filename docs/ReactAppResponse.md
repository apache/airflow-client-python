# ReactAppResponse

Serializer for React App Plugin responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applies_to** | **Dict[str, List[str]]** | Serializer for the optional scoping criteria of a UI plugin.  An open map of dotted field path to the values that path may take -- not a closed set of criteria. &#x60;&#x60;{\&quot;state\&quot;: [\&quot;failed\&quot;], \&quot;dag.tags.name\&quot;: [\&quot;ml\&quot;]}&#x60;&#x60; scopes to failed entities of ml-tagged Dags. An unqualified path is rooted at the entity the &#x60;&#x60;destination&#x60;&#x60; is about; a path may instead name a related record (&#x60;&#x60;dag&#x60;&#x60;, &#x60;&#x60;dag_run&#x60;&#x60;, &#x60;&#x60;task&#x60;&#x60;, &#x60;&#x60;task_instance&#x60;&#x60;) as its first segment. Matching is equality against the listed values, OR within a path and AND across paths, and is evaluated client-side. | [optional] 
**bundle_url** | **str** |  | 
**category** | **str** |  | [optional] 
**destination** | **str** |  | [optional] [default to 'nav']
**icon** | **str** |  | [optional] 
**icon_dark_mode** | **str** |  | [optional] 
**name** | **str** |  | 
**nav_top_level** | **bool** |  | [optional] 
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


