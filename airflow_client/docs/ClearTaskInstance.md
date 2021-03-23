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

# ClearTaskInstance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **bool** | If set, don&#39;t actually run this operation. The response will contain a list of task instances planned to be cleaned, but not modified in any way.  | [optional]  if omitted the server will use the default value of True
**start_date** | **str** | The minimum execution date to clear. | [optional] 
**end_date** | **str** | The maximum execution date to clear. | [optional] 
**only_failed** | **bool** | Only clear failed tasks. | [optional]  if omitted the server will use the default value of True
**only_running** | **bool** | Only clear running tasks. | [optional]  if omitted the server will use the default value of False
**include_subdags** | **bool** | Clear tasks in subdags and clear external tasks indicated by ExternalTaskMarker. | [optional] 
**include_parentdag** | **bool** | Clear tasks in the parent dag of the subdag. | [optional] 
**reset_dag_runs** | **bool** | Set state of DAG runs to RUNNING. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


