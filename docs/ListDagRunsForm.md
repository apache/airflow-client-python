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

# ListDagRunsForm


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_by** | **str** | The name of the field to order the results by. Prefix a field name with &#x60;-&#x60; to reverse the sort order.  *New in version 2.1.0*  | [optional] 
**page_offset** | **int** | The number of items to skip before starting to collect the result set. | [optional] 
**page_limit** | **int** | The numbers of items to return. | [optional]  if omitted the server will use the default value of 100
**dag_ids** | **[str]** | Return objects with specific DAG IDs. The value can be repeated to retrieve multiple matching values (OR condition). | [optional] 
**states** | **[str]** | Return objects with specific states. The value can be repeated to retrieve multiple matching values (OR condition). | [optional] 
**execution_date_gte** | **datetime** | Returns objects greater or equal to the specified date.  This can be combined with execution_date_lte key to receive only the selected period.  | [optional] 
**execution_date_lte** | **datetime** | Returns objects less than or equal to the specified date.  This can be combined with execution_date_gte key to receive only the selected period.  | [optional] 
**start_date_gte** | **datetime** | Returns objects greater or equal the specified date.  This can be combined with start_date_lte key to receive only the selected period.  | [optional] 
**start_date_lte** | **datetime** | Returns objects less or equal the specified date.  This can be combined with start_date_gte parameter to receive only the selected period  | [optional] 
**end_date_gte** | **datetime** | Returns objects greater or equal the specified date.  This can be combined with end_date_lte parameter to receive only the selected period.  | [optional] 
**end_date_lte** | **datetime** | Returns objects less than or equal to the specified date.  This can be combined with end_date_gte parameter to receive only the selected period.  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


