# AssetStateStoreWriterKind

Identifies what kind of writer last updated an asset state store entry.  ``TASK`` — written by a task via the execution API. ``WATCHER`` — written by a ``BaseEventTrigger`` (no task instance). ``API`` — written directly through the Core API (e.g. manual admin write).

## Enum

* `TASK` (value: `'task'`)

* `WATCHER` (value: `'watcher'`)

* `API` (value: `'api'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


