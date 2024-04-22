# TaskState

Task state.  *Changed in version 2.0.2*&#58; 'removed' is added as a possible value.  *Changed in version 2.2.0*&#58; 'deferred' is added as a possible value.  *Changed in version 2.4.0*&#58; 'sensing' state has been removed. *Changed in version 2.4.2*&#58; 'restarting' is added as a possible value  *Changed in version 2.7.0*&#58; Field becomes nullable and null primitive is added as a possible value. *Changed in version 2.7.0*&#58; 'none' state is deprecated in favor of null. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Task state.  *Changed in version 2.0.2*&amp;#58; &#39;removed&#39; is added as a possible value.  *Changed in version 2.2.0*&amp;#58; &#39;deferred&#39; is added as a possible value.  *Changed in version 2.4.0*&amp;#58; &#39;sensing&#39; state has been removed. *Changed in version 2.4.2*&amp;#58; &#39;restarting&#39; is added as a possible value  *Changed in version 2.7.0*&amp;#58; Field becomes nullable and null primitive is added as a possible value. *Changed in version 2.7.0*&amp;#58; &#39;none&#39; state is deprecated in favor of null.  |  must be one of ["null", "success", "running", "failed", "upstream_failed", "skipped", "up_for_retry", "up_for_reschedule", "queued", "none", "scheduled", "deferred", "removed", "restarting", ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


