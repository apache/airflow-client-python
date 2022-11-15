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

# Apache Airflow Python Client

> **_NOTE:_**  The Apache Airflow Client is still under active development and some methods
> or APIs might be broken. Please raise an issue in github if you encounter any such issues.



## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

You can install directly using pip:

```sh
pip install apache-airflow-client
````

### Setuptools

Or install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
git clone git@github.com:apache/airflow-client-python.git
cd airflow-client-python
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import airflow_client.client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import airflow_client.client
from pprint import pprint
from airflow_client.client.api import config_api

#
# In case of the basic authentication below. Make sure:
#  - Airflow is configured with the basic_auth as backend:
#     auth_backend = airflow.api.auth.backend.basic_auth
#  - Make sure that the client has been generated with securitySchema Basic.

# Configure HTTP basic authorization: Basic
configuration = airflow_client.client.Configuration(
    host="http://localhost/api/v1",
    username='admin',
    password='admin'
)


# Enter a context with an instance of the API client
with airflow_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = config_api.ConfigApi(api_client)

    try:
        # Get current configuration
        api_response = api_instance.get_config()
        pprint(api_response)
    except airflow_client.client.ApiException as e:
        print("Exception when calling ConfigApi->get_config: %s\n" % e)
```

See [README](./airflow_client/README.md#documentation-for-api-endpoints) for full client API documentation.

## Release Process

Typically releases are done coinciding with major and minor releases to Airflow. Therefore a release of (for example) 2.3.0 of this client
would correspond with 2.3.X of Airflow.

The Python client is generated using Airflow's [openapi spec](https://github.com/apache/airflow/blob/master/clients/gen/python.sh).
To update the client for new APIs do the following steps:

```bash
# clone this repo
git clone git@github.com:apache/airflow-client-python.git

# clone Airflow repo (if not already)
git clone git@github.com:apache/airflow.git
```
Edit the file `airflow/airflow/api_connexion/openapi/v1.yaml`
Make sure it has the following `securitySchema`s listed under security `section`
```yaml
security:
  - Basic: []
  - GoogleOpenId: []
  - Kerberos: []
```
If your deployment of Airflow uses any different authentication mechanism than the three listed above, you might need to make further changes to the `v1.yaml` and generate your own client, see [OpenAPI Schema specification](https://swagger.io/docs/specification/authentication/) for details.
(*These changes should not be commited to the upstream `v1.yaml` [as it will generate misleading openapi documentaion](https://github.com/apache/airflow/pull/17174)*)

Update the VERSION string in setup.py with the corresponding new version string.

```bash
cd airflow

# bump up the version in python.sh & run the following command
./clients/gen/python.sh airflow/api_connexion/openapi/v1.yaml ../airflow-client-python/airflow_client

# raise a PR in github for both the repos (airflow & airflow-client-python)
```
