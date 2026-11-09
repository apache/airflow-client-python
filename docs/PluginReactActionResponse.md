# PluginReactActionResponse

Serializer for a UI action that mounts a React component behind a button.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** | **str** |  | 
**applies_to** | **Dict[str, List[str]]** | Serializer for the optional scoping criteria of a UI plugin.  An open map of dotted field path to the values that path may take -- not a closed set of criteria. &#x60;&#x60;{\&quot;state\&quot;: [\&quot;failed\&quot;], \&quot;dag.tags.name\&quot;: [\&quot;ml\&quot;]}&#x60;&#x60; scopes to failed entities of ml-tagged Dags. An unqualified path is rooted at the entity the &#x60;&#x60;destination&#x60;&#x60; is about; a path may instead name a related record (&#x60;&#x60;dag&#x60;&#x60;, &#x60;&#x60;dag_run&#x60;&#x60;, &#x60;&#x60;task&#x60;&#x60;, &#x60;&#x60;task_instance&#x60;&#x60;) as its first segment. Matching is equality against the listed values, OR within a path and AND across paths, and is evaluated client-side. | [optional] 
**bundle_url** | **str** |  | 
**destination** | **str** |  | 
**icon** | **str** |  | [optional] 
**icon_dark_mode** | **str** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from airflow_client.client.models.plugin_react_action_response import PluginReactActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PluginReactActionResponse from a JSON string
plugin_react_action_response_instance = PluginReactActionResponse.from_json(json)
# print the JSON string representation of the object
print(PluginReactActionResponse.to_json())

# convert the object into a dict
plugin_react_action_response_dict = plugin_react_action_response_instance.to_dict()
# create an instance of PluginReactActionResponse from a dict
plugin_react_action_response_from_dict = PluginReactActionResponse.from_dict(plugin_react_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


