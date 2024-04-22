# User

A user object with sensitive data.  *New in version 2.1.0* 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool, none_type** | Whether the user is active | [optional] [readonly] 
**changed_on** | **str, none_type** | The date user was changed | [optional] [readonly] 
**created_on** | **str, none_type** | The date user was created | [optional] [readonly] 
**email** | **str** | The user&#39;s email.  *Changed in version 2.2.0*&amp;#58; A minimum character length requirement (&#39;minLength&#39;) is added.  | [optional] 
**failed_login_count** | **int, none_type** | The number of times the login failed | [optional] [readonly] 
**first_name** | **str** | The user&#39;s first name.  *Changed in version 2.4.0*&amp;#58; The requirement for this to be non-empty was removed.  | [optional] 
**last_login** | **str, none_type** | The last user login | [optional] [readonly] 
**last_name** | **str** | The user&#39;s last name.  *Changed in version 2.4.0*&amp;#58; The requirement for this to be non-empty was removed.  | [optional] 
**login_count** | **int, none_type** | The login count | [optional] [readonly] 
**roles** | [**[UserCollectionItemRoles]**](UserCollectionItemRoles.md) | User roles.  *Changed in version 2.2.0*&amp;#58; Field is no longer read-only.  | [optional] 
**username** | **str** | The username.  *Changed in version 2.2.0*&amp;#58; A minimum character length requirement (&#39;minLength&#39;) is added.  | [optional] 
**password** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


