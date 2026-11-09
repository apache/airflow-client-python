# UiActionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** | **str** |  | 
**applies_to** | **Dict[str, List[str]]** | Serializer for the optional scoping criteria of a UI plugin.  An open map of dotted field path to the values that path may take -- not a closed set of criteria. &#x60;&#x60;{\&quot;state\&quot;: [\&quot;failed\&quot;], \&quot;dag.tags.name\&quot;: [\&quot;ml\&quot;]}&#x60;&#x60; scopes to failed entities of ml-tagged Dags. An unqualified path is rooted at the entity the &#x60;&#x60;destination&#x60;&#x60; is about; a path may instead name a related record (&#x60;&#x60;dag&#x60;&#x60;, &#x60;&#x60;dag_run&#x60;&#x60;, &#x60;&#x60;task&#x60;&#x60;, &#x60;&#x60;task_instance&#x60;&#x60;) as its first segment. Matching is equality against the listed values, OR within a path and AND across paths, and is evaluated client-side. | [optional] 
**destination** | **str** |  | 
**href** | **str** |  | 
**icon** | **str** |  | [optional] 
**icon_dark_mode** | **str** |  | [optional] 
**name** | **str** |  | 
**bundle_url** | **str** |  | 

## Example

```python
from airflow_client.client.models.ui_actions_inner import UiActionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of UiActionsInner from a JSON string
ui_actions_inner_instance = UiActionsInner.from_json(json)
# print the JSON string representation of the object
print(UiActionsInner.to_json())

# convert the object into a dict
ui_actions_inner_dict = ui_actions_inner_instance.to_dict()
# create an instance of UiActionsInner from a dict
ui_actions_inner_from_dict = UiActionsInner.from_dict(ui_actions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


