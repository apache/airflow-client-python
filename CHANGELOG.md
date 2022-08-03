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

# v2.3.0

Apache Airflow API version: 2.3.x

### Major changes:

- NA

### Major fixes:

- NA

### New API supported:

- PATCH /dags | Update DAGs
- GET /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/{map_index} | Get a mapped task instance
- GET /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/listMapped | List mapped task instances

# v2.2.0

Apache Airflow API version: 2.2.x

### Major changes:

- Client code is generated using OpenApi's 5.3.0 generator CLI

### Major fixes:

- NA

### New API supported:

- POST /connections/test | Test a connection
- DELETE /dags/{dag_id} | Delete a DAG
- PATCH /dags/{dag_id}/dagRuns/{dag_run_id} | Modify a DAG run
- DELETE /users/{username} | Delete a user
- PATCH /users/{username} | Update a user
- POST /users | Create a user

# v2.1.0

Apache Airflow API version: 2.1.x

### Major changes:

 - Client code is generated using OpenApi's 5.1.1 generator CLI

### Major fixes:

 - Fixed the iteration issue on array items caused by unsupported class 'object' (issue #15)

### New API supported:

 - Permissions
 - Plugins
 - Providers
 - Roles
 - Users

# v2.0.0

Apache Airflow API version: 2.0.x

Initial version of the Python client.
