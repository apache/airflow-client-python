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

"""
    Airflow API (Stable)

    The version of the OpenAPI document: 1.0.0
    Contact: dev@airflow.apache.org
    Generated by: https://openapi-generator.tech
"""

from os import path
from setuptools import setup, find_packages  # noqa: H301


NAME = "airflow-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "urllib3 >= 1.25.3",
    "python-dateutil",
]

THIS_DIR = path.abspath(path.dirname(__file__))
with open(path.join(THIS_DIR, 'README.md'), encoding='utf-8') as f:
    LONG_DESC = f.read()

setup(
    name=NAME,
    version=VERSION,
    description="Airflow API (Stable)",
    author="Apache Software Foundation",
    author_email="dev@airflow.apache.org",
    url="https://airflow.apache.org/",
    keywords=["OpenAPI", "OpenAPI-Generator", "Airflow API (Stable)"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache License 2.0",
    long_description=LONG_DESC,
    long_description_content_type="text/markdown"
)
