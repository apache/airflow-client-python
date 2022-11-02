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

# Task

For details see: [airflow.models.BaseOperator](https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/models/index.html#airflow.models.BaseOperator) 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_ref** | [**ClassReference**](ClassReference.md) |  | [optional] 
**task_id** | **str** |  | [optional] [readonly] 
**owner** | **str** |  | [optional] [readonly] 
**start_date** | **datetime** |  | [optional] [readonly] 
**end_date** | **datetime, none_type** |  | [optional] [readonly] 
**trigger_rule** | [**TriggerRule**](TriggerRule.md) |  | [optional] 
**extra_links** | [**[TaskExtraLinks]**](TaskExtraLinks.md) |  | [optional] [readonly] 
**depends_on_past** | **bool** |  | [optional] [readonly] 
**is_mapped** | **bool** |  | [optional] [readonly] 
**wait_for_downstream** | **bool** |  | [optional] [readonly] 
**retries** | **float** |  | [optional] [readonly] 
**queue** | **str, none_type** |  | [optional] [readonly] 
**pool** | **str** |  | [optional] [readonly] 
**pool_slots** | **float** |  | [optional] [readonly] 
**execution_timeout** | [**TimeDelta**](TimeDelta.md) |  | [optional] 
**retry_delay** | [**TimeDelta**](TimeDelta.md) |  | [optional] 
**retry_exponential_backoff** | **bool** |  | [optional] [readonly] 
**priority_weight** | **float** |  | [optional] [readonly] 
**weight_rule** | [**WeightRule**](WeightRule.md) |  | [optional] 
**ui_color** | [**Color**](Color.md) |  | [optional] 
**ui_fgcolor** | [**Color**](Color.md) |  | [optional] 
**template_fields** | **[str]** |  | [optional] [readonly] 
**sub_dag** | [**DAG**](DAG.md) |  | [optional] 
**downstream_task_ids** | **[str]** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


