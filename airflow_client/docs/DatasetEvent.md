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

# DatasetEvent

A dataset event.  *New in version 2.4.0* 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_id** | **int** | The dataset id | [optional] 
**dataset_uri** | **str** | The URI of the dataset | [optional] 
**extra** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | The dataset event extra | [optional] 
**source_dag_id** | **str, none_type** | The DAG ID that updated the dataset. | [optional] 
**source_task_id** | **str, none_type** | The task ID that updated the dataset. | [optional] 
**source_run_id** | **str, none_type** | The DAG run ID that updated the dataset. | [optional] 
**source_map_index** | **int, none_type** | The task map index that updated the dataset. | [optional] 
**created_dagruns** | [**[BasicDAGRun]**](BasicDAGRun.md) |  | [optional] 
**timestamp** | **str** | The dataset event creation time | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


