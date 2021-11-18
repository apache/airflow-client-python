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

# User

A user object with sensitive data

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | The user firstname | [optional] 
**last_name** | **str** | The user lastname | [optional] 
**username** | **str** | The username | [optional] 
**email** | **str** | The user&#39;s email | [optional] 
**active** | **bool, none_type** | Whether the user is active | [optional] [readonly] 
**last_login** | **str, none_type** | The last user login | [optional] [readonly] 
**login_count** | **int, none_type** | The login count | [optional] [readonly] 
**failed_login_count** | **int, none_type** | The number of times the login failed | [optional] [readonly] 
**roles** | [**[UserCollectionItemRoles]**](UserCollectionItemRoles.md) | User roles | [optional] 
**created_on** | **str, none_type** | The date user was created | [optional] [readonly] 
**changed_on** | **str, none_type** | The date user was changed | [optional] [readonly] 
**password** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


