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

# TaskInstance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** |  | [optional] 
**dag_id** | **str** |  | [optional] 
**dag_run_id** | **str** | The DagRun ID for this task instance  *New in version 2.3.0*  | [optional] 
**execution_date** | **str** |  | [optional] 
**start_date** | **str, none_type** |  | [optional] 
**end_date** | **str, none_type** |  | [optional] 
**duration** | **float, none_type** |  | [optional] 
**state** | [**TaskState**](TaskState.md) |  | [optional] 
**try_number** | **int** |  | [optional] 
**map_index** | **int** |  | [optional] 
**max_tries** | **int** |  | [optional] 
**hostname** | **str** |  | [optional] 
**unixname** | **str** |  | [optional] 
**pool** | **str** |  | [optional] 
**pool_slots** | **int** |  | [optional] 
**queue** | **str, none_type** |  | [optional] 
**priority_weight** | **int, none_type** |  | [optional] 
**operator** | **str, none_type** | *Changed in version 2.1.1*&amp;#58; Field becomes nullable.  | [optional] 
**queued_when** | **str, none_type** |  | [optional] 
**pid** | **int, none_type** |  | [optional] 
**executor_config** | **str** |  | [optional] 
**sla_miss** | [**SLAMiss**](SLAMiss.md) |  | [optional] 
**rendered_fields** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | JSON object describing rendered fields.  *New in version 2.3.0*  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


