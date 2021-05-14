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
from airflow_client.client.api import config_api, dag_api

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
    host="http://localhost/api/v1",
    username='admin',
    password='admin'
)


with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    dag_api_instance = dag_api.DAGApi(api_client)

    try:
        # Get current configuration
        api_response = dag_api_instance.get_dags()
        pprint(api_response)
    except airflow_client.client.ApiException as e:
        print("Exception when calling DagAPI->get_dags: %s\n" % e)


# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    dag_api_instance = config_api.ConfigApi(api_client)

    try:
        # Get current configuration
        api_response = dag_api_instance.get_config()
        pprint(api_response)
    except airflow_client.client.ApiException as e:
        print("Exception when calling ConfigApi->get_config: %s\n" % e)
