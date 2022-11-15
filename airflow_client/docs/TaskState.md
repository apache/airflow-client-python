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

# TaskState

Task state.  *Changed in version 2.0.2*&#58; 'removed' is added as a possible value.  *Changed in version 2.2.0*&#58; 'deferred' is added as a possible value.  *Changed in version 2.4.0*&#58; 'sensing' state has been removed. *Changed in version 2.4.2*&#58; 'restarting' is added as a possible value 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Task state.  *Changed in version 2.0.2*&amp;#58; &#39;removed&#39; is added as a possible value.  *Changed in version 2.2.0*&amp;#58; &#39;deferred&#39; is added as a possible value.  *Changed in version 2.4.0*&amp;#58; &#39;sensing&#39; state has been removed. *Changed in version 2.4.2*&amp;#58; &#39;restarting&#39; is added as a possible value  |  must be one of ["success", "running", "failed", "upstream_failed", "skipped", "up_for_retry", "up_for_reschedule", "queued", "none", "scheduled", "deferred", "removed", "restarting", ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


