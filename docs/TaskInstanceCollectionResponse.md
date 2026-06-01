# TaskInstanceCollectionResponse

Task instance collection response supporting both offset and cursor pagination.  A single flat model is used instead of a discriminated union (``Annotated[Offset | Cursor, Field(discriminator=...)]``) because the OpenAPI ``oneOf`` + ``discriminator`` construct is not handled correctly by ``@hey-api/openapi-ts`` / ``@7nohe/openapi-react-query-codegen``: return types degrade to ``unknown`` in JSDoc and can produce incorrect TypeScript types (see hey-api/openapi-ts#1613, #3270).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_instances** | [**List[TaskInstanceResponse]**](TaskInstanceResponse.md) |  | 
**total_entries** | **int** | Total number of matching items. Populated for offset pagination, &#x60;&#x60;null&#x60;&#x60; when using cursor pagination. | [optional] 
**next_cursor** | **str** | Token pointing to the next page. Populated for cursor pagination, &#x60;&#x60;null&#x60;&#x60; when using offset pagination or when there is no next page. | [optional] 
**previous_cursor** | **str** | Token pointing to the previous page. Populated for cursor pagination, &#x60;&#x60;null&#x60;&#x60; when using offset pagination or when on the first page. | [optional] 

## Example

```python
from airflow_client.client.models.task_instance_collection_response import TaskInstanceCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TaskInstanceCollectionResponse from a JSON string
task_instance_collection_response_instance = TaskInstanceCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(TaskInstanceCollectionResponse.to_json())

# convert the object into a dict
task_instance_collection_response_dict = task_instance_collection_response_instance.to_dict()
# create an instance of TaskInstanceCollectionResponse from a dict
task_instance_collection_response_from_dict = TaskInstanceCollectionResponse.from_dict(task_instance_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


