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

# DAGDetailAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timezone** | **str** |  | [optional] 
**catchup** | **bool** |  | [optional] [readonly] 
**orientation** | **str** |  | [optional] [readonly] 
**concurrency** | **float** |  | [optional] [readonly] 
**start_date** | **datetime, none_type** | The DAG&#39;s start date.  *Changed in version 2.0.1*&amp;#58; Field becomes nullable.  | [optional] [readonly] 
**dag_run_timeout** | [**TimeDelta**](TimeDelta.md) |  | [optional] 
**doc_md** | **str, none_type** |  | [optional] [readonly] 
**default_view** | **str** |  | [optional] [readonly] 
**params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | User-specified DAG params.  *New in version 2.0.1*  | [optional] [readonly] 
**end_date** | **datetime, none_type** | The DAG&#39;s end date.  *New in version 2.3.0*.  | [optional] [readonly] 
**is_paused_upon_creation** | **bool, none_type** | Whether the DAG is paused upon creation.  *New in version 2.3.0*  | [optional] [readonly] 
**last_parsed** | **datetime, none_type** | The last time the DAG was parsed.  *New in version 2.3.0*  | [optional] [readonly] 
**template_search_path** | **[str], none_type** | The template search path.  *New in version 2.3.0*  | [optional] 
**render_template_as_native_obj** | **bool, none_type** | Whether to render templates as native Python objects.  *New in version 2.3.0*  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


