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

# PluginCollectionItem

A plugin Item.  *New in version 2.1.0* 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the plugin | [optional] 
**hooks** | **[str, none_type]** | The plugin hooks | [optional] 
**executors** | **[str, none_type]** | The plugin executors | [optional] 
**macros** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type]** | The plugin macros | [optional] 
**flask_blueprints** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type]** | The flask blueprints | [optional] 
**appbuilder_views** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type]** | The appuilder views | [optional] 
**appbuilder_menu_items** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type]** | The Flask Appbuilder menu items | [optional] 
**global_operator_extra_links** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type]** | The global operator extra links | [optional] 
**operator_extra_links** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type]** | Operator extra links | [optional] 
**source** | **str, none_type** | The plugin source | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


