# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
import airflow_client.client
from pprint import pprint
from airflow_client.client.api import config_api, dag_api, dag_run_api
from airflow_client.client.model.dag_run import DAGRun

# The client must use the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
#
# In case of the basic authentication below, make sure that Airflow is
# configured with the basic_auth as backend:
#
# auth_backend = airflow.api.auth.backend.basic_auth
#
# Make sure that your user/name are configured properly

# Configure HTTP basic authorization: Basic
configuration = airflow_client.client.Configuration(
    host="http://localhost:8080/api/v1",
    username='admin',
    password='admin'
)

dag_id = "example_bash_operator"

# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Get current configuration
    conf_api_instance = config_api.ConfigApi(api_client)
    try:
        api_response = conf_api_instance.get_config()
        pprint(api_response)
    except airflow_client.client.OpenApiException as e:
        print("Exception when calling ConfigApi->get_config: %s\n" % e)


    # Get dag list
    dag_api_instance = dag_api.DAGApi(api_client)
    try:
        api_response = dag_api_instance.get_dags()
        pprint(api_response)
    except airflow_client.client.OpenApiException as e:
        print("Exception when calling DagAPI->get_dags: %s\n" % e)


    # Get tasks for a DAG (TODO: issue#20)
    try:
        api_response = dag_api_instance.get_tasks(dag_id)
        pprint(api_response)
    except airflow_client.client.exceptions.OpenApiException as e:
        print("Exception when calling DagAPI->get_tasks: %s\n" % e)


    # Trigger a dag run (TODO: issue#21)
    dag_run_api_instance = dag_run_api.DAGRunApi(api_client)
    try:
        # Create a DAGRun object
        dag_run = DAGRun(
            dag_run_id='some_test_run',
            dag_id=dag_id,
            external_trigger=True,
        )
        api_response = dag_run_api_instance.post_dag_run(dag_id, dag_run)
        pprint(api_response)
    except airflow_client.client.exceptions.OpenApiException as e:
        print("Exception when calling DAGRunAPI->post_dag_run: %s\n" % e)