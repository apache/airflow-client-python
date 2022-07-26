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

# UpdateTaskInstancesState


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **bool** | If set, don&#39;t actually run this operation. The response will contain a list of task instances planned to be affected, but won&#39;t be modified in any way.  | [optional]  if omitted the server will use the default value of True
**task_id** | **str** | The task ID. | [optional] 
**execution_date** | **str** | The execution date. Either set this or dag_run_id but not both. | [optional] 
**dag_run_id** | **str** | The task instance&#39;s DAG run ID. Either set this or execution_date but not both.  *New in version 2.3.0*  | [optional] 
**include_upstream** | **bool** | If set to true, upstream tasks are also affected. | [optional] 
**include_downstream** | **bool** | If set to true, downstream tasks are also affected. | [optional] 
**include_future** | **bool** | If set to True, also tasks from future DAG Runs are affected. | [optional] 
**include_past** | **bool** | If set to True, also tasks from past DAG Runs are affected. | [optional] 
**new_state** | **str** | Expected new state. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


