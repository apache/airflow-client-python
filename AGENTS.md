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

# Apache Airflow Python Client — Agent Instructions

This file is read by automated agents (security scanners, code
analyzers, AI assistants) operating on this repository. It
points them at the human-authored references they should
consult before producing output.

## Security Model

The authoritative security reference for this client is the
Apache Airflow Security Model:

  https://airflow.apache.org/docs/apache-airflow/stable/security/security_model.html

(Repo source: [`apache/airflow:airflow-core/docs/security/security_model.rst`](https://github.com/apache/airflow/blob/main/airflow-core/docs/security/security_model.rst).)

This client library inherits Apache Airflow's security model.
In particular, the *"What is NOT considered a security
vulnerability"* section enumerates recurring non-findings —
agents should consult it before reporting issues against the
Airflow API surface this client wraps.

Client-specific concerns (TLS configuration, token handling,
retry/backoff behaviour, connection lifecycle) follow the
guidance in the upstream Airflow model unless explicitly
documented otherwise in this repository.
