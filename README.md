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


## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

You can install directly using pip:

```sh
pip install git+https://github.com/apache/airflow-client-python/airflow.git
````

### Setuptools

Or install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import airflow_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import airflow_client
from pprint import pprint
from airflow_client.api import config_api
from airflow_client.model.config import Config
from airflow_client.model.error import Error
# Defining the host is optional and defaults to http://localhost/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = airflow_client.Configuration(
    host = "http://localhost/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = airflow_client.Configuration(
    host = "http://localhost/api/v1",
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)


# Enter a context with an instance of the API client
with airflow_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = config_api.ConfigApi(api_client)
    
    try:
        # Get current configuration
        api_response = api_instance.get_config()
        pprint(api_response)
    except airflow_client.ApiException as e:
        print("Exception when calling ConfigApi->get_config: %s\n" % e)
```

See [README](./airflow/README.md#documentation-for-api-endpoints) for full client API documentation.

## Release Process

The Python client is generated using Airflow's [openapi spec](https://github.com/apache/airflow/blob/master/clients/gen/python.sh). 
To update the client for new APIs do the following steps:

```bash
# clone this repo
git clone git@github.com:apache/airflow-client-python.git

# clone Airflow repo (if not already)
git clone git@github.com:apache/airflow.git
cd airflow

# bump up the version in python.sh & run the following command 
./clients/gen/python.sh airflow/api_connexion/openapi/v1.yaml ../airflow-client-python/airflow

# raise a PR in github
```
