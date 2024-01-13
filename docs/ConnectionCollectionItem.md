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

# ConnectionCollectionItem

Connection collection item. The password and extra fields are only available when retrieving a single object due to the sensitivity of this data. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **str** | The connection ID. | [optional] 
**conn_type** | **str** | The connection type. | [optional] 
**description** | **str, none_type** | The description of the connection. | [optional] 
**host** | **str, none_type** | Host of the connection. | [optional] 
**login** | **str, none_type** | Login of the connection. | [optional] 
**schema** | **str, none_type** | Schema of the connection. | [optional] 
**port** | **int, none_type** | Port of the connection. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


