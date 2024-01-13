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

# EventLog

Log of user operations via CLI or Web UI.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_log_id** | **int** | The event log ID | [optional] [readonly] 
**when** | **datetime** | The time when these events happened. | [optional] [readonly] 
**dag_id** | **str, none_type** | The DAG ID | [optional] [readonly] 
**task_id** | **str, none_type** | The DAG ID | [optional] [readonly] 
**event** | **str** | A key describing the type of event. | [optional] [readonly] 
**execution_date** | **datetime, none_type** | When the event was dispatched for an object having execution_date, the value of this field.  | [optional] [readonly] 
**owner** | **str** | Name of the user who triggered these events a. | [optional] [readonly] 
**extra** | **str, none_type** | Other information that was not included in the other fields, e.g. the complete CLI command.  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


