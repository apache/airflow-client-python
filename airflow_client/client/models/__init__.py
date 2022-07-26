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

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from airflow_client.client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from airflow_client.client.model.action import Action
from airflow_client.client.model.action_collection import ActionCollection
from airflow_client.client.model.action_collection_all_of import ActionCollectionAllOf
from airflow_client.client.model.action_resource import ActionResource
from airflow_client.client.model.class_reference import ClassReference
from airflow_client.client.model.clear_task_instance import ClearTaskInstance
from airflow_client.client.model.collection_info import CollectionInfo
from airflow_client.client.model.color import Color
from airflow_client.client.model.config import Config
from airflow_client.client.model.config_option import ConfigOption
from airflow_client.client.model.config_section import ConfigSection
from airflow_client.client.model.connection import Connection
from airflow_client.client.model.connection_all_of import ConnectionAllOf
from airflow_client.client.model.connection_collection import ConnectionCollection
from airflow_client.client.model.connection_collection_all_of import ConnectionCollectionAllOf
from airflow_client.client.model.connection_collection_item import ConnectionCollectionItem
from airflow_client.client.model.connection_test import ConnectionTest
from airflow_client.client.model.cron_expression import CronExpression
from airflow_client.client.model.dag import DAG
from airflow_client.client.model.dag_collection import DAGCollection
from airflow_client.client.model.dag_collection_all_of import DAGCollectionAllOf
from airflow_client.client.model.dag_detail import DAGDetail
from airflow_client.client.model.dag_detail_all_of import DAGDetailAllOf
from airflow_client.client.model.dag_run import DAGRun
from airflow_client.client.model.dag_run_collection import DAGRunCollection
from airflow_client.client.model.dag_run_collection_all_of import DAGRunCollectionAllOf
from airflow_client.client.model.dag_state import DagState
from airflow_client.client.model.error import Error
from airflow_client.client.model.event_log import EventLog
from airflow_client.client.model.event_log_collection import EventLogCollection
from airflow_client.client.model.event_log_collection_all_of import EventLogCollectionAllOf
from airflow_client.client.model.extra_link import ExtraLink
from airflow_client.client.model.extra_link_collection import ExtraLinkCollection
from airflow_client.client.model.health_info import HealthInfo
from airflow_client.client.model.health_status import HealthStatus
from airflow_client.client.model.import_error import ImportError
from airflow_client.client.model.import_error_collection import ImportErrorCollection
from airflow_client.client.model.import_error_collection_all_of import ImportErrorCollectionAllOf
from airflow_client.client.model.inline_response200 import InlineResponse200
from airflow_client.client.model.inline_response2001 import InlineResponse2001
from airflow_client.client.model.list_dag_runs_form import ListDagRunsForm
from airflow_client.client.model.list_task_instance_form import ListTaskInstanceForm
from airflow_client.client.model.metadatabase_status import MetadatabaseStatus
from airflow_client.client.model.plugin_collection import PluginCollection
from airflow_client.client.model.plugin_collection_all_of import PluginCollectionAllOf
from airflow_client.client.model.plugin_collection_item import PluginCollectionItem
from airflow_client.client.model.pool import Pool
from airflow_client.client.model.pool_collection import PoolCollection
from airflow_client.client.model.pool_collection_all_of import PoolCollectionAllOf
from airflow_client.client.model.provider import Provider
from airflow_client.client.model.provider_collection import ProviderCollection
from airflow_client.client.model.relative_delta import RelativeDelta
from airflow_client.client.model.resource import Resource
from airflow_client.client.model.role import Role
from airflow_client.client.model.role_collection import RoleCollection
from airflow_client.client.model.role_collection_all_of import RoleCollectionAllOf
from airflow_client.client.model.sla_miss import SLAMiss
from airflow_client.client.model.schedule_interval import ScheduleInterval
from airflow_client.client.model.scheduler_status import SchedulerStatus
from airflow_client.client.model.tag import Tag
from airflow_client.client.model.task import Task
from airflow_client.client.model.task_collection import TaskCollection
from airflow_client.client.model.task_extra_links import TaskExtraLinks
from airflow_client.client.model.task_instance import TaskInstance
from airflow_client.client.model.task_instance_collection import TaskInstanceCollection
from airflow_client.client.model.task_instance_collection_all_of import TaskInstanceCollectionAllOf
from airflow_client.client.model.task_instance_reference import TaskInstanceReference
from airflow_client.client.model.task_instance_reference_collection import TaskInstanceReferenceCollection
from airflow_client.client.model.task_state import TaskState
from airflow_client.client.model.time_delta import TimeDelta
from airflow_client.client.model.trigger_rule import TriggerRule
from airflow_client.client.model.update_dag_run_state import UpdateDagRunState
from airflow_client.client.model.update_task_instances_state import UpdateTaskInstancesState
from airflow_client.client.model.user import User
from airflow_client.client.model.user_all_of import UserAllOf
from airflow_client.client.model.user_collection import UserCollection
from airflow_client.client.model.user_collection_all_of import UserCollectionAllOf
from airflow_client.client.model.user_collection_item import UserCollectionItem
from airflow_client.client.model.user_collection_item_roles import UserCollectionItemRoles
from airflow_client.client.model.variable import Variable
from airflow_client.client.model.variable_all_of import VariableAllOf
from airflow_client.client.model.variable_collection import VariableCollection
from airflow_client.client.model.variable_collection_all_of import VariableCollectionAllOf
from airflow_client.client.model.variable_collection_item import VariableCollectionItem
from airflow_client.client.model.version_info import VersionInfo
from airflow_client.client.model.weight_rule import WeightRule
from airflow_client.client.model.x_com import XCom
from airflow_client.client.model.x_com_all_of import XComAllOf
from airflow_client.client.model.x_com_collection import XComCollection
from airflow_client.client.model.x_com_collection_all_of import XComCollectionAllOf
from airflow_client.client.model.x_com_collection_item import XComCollectionItem
