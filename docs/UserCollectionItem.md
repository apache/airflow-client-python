<!--
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements.  See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership.  The ASF licenses this file
 to you under the Apache License, Version 2.0 (the
 "License"); you may not use this file except in compliance
 with the License.  You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing,
 software distributed under the License is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied.  See the License for the
 specific language governing permissions and limitations
 under the License.
 -->

# UserCollectionItem

A user object.  *New in version 2.1.0* 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | The user&#39;s first name.  *Changed in version 2.4.0*&amp;#58; The requirement for this to be non-empty was removed.  | [optional] 
**last_name** | **str** | The user&#39;s last name.  *Changed in version 2.4.0*&amp;#58; The requirement for this to be non-empty was removed.  | [optional] 
**username** | **str** | The username.  *Changed in version 2.2.0*&amp;#58; A minimum character length requirement (&#39;minLength&#39;) is added.  | [optional] 
**email** | **str** | The user&#39;s email.  *Changed in version 2.2.0*&amp;#58; A minimum character length requirement (&#39;minLength&#39;) is added.  | [optional] 
**active** | **bool, none_type** | Whether the user is active | [optional] [readonly] 
**last_login** | **str, none_type** | The last user login | [optional] [readonly] 
**login_count** | **int, none_type** | The login count | [optional] [readonly] 
**failed_login_count** | **int, none_type** | The number of times the login failed | [optional] [readonly] 
**roles** | [**[UserCollectionItemRoles]**](UserCollectionItemRoles.md) | User roles.  *Changed in version 2.2.0*&amp;#58; Field is no longer read-only.  | [optional] 
**created_on** | **str, none_type** | The date user was created | [optional] [readonly] 
**changed_on** | **str, none_type** | The date user was changed | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


