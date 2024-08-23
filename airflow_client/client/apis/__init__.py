
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.config_api import ConfigApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from airflow_client.client.api.config_api import ConfigApi
from airflow_client.client.api.connection_api import ConnectionApi
from airflow_client.client.api.dag_api import DAGApi
from airflow_client.client.api.dag_run_api import DAGRunApi
from airflow_client.client.api.dag_stats_api import DagStatsApi
from airflow_client.client.api.dag_warning_api import DagWarningApi
from airflow_client.client.api.dataset_api import DatasetApi
from airflow_client.client.api.event_log_api import EventLogApi
from airflow_client.client.api.import_error_api import ImportErrorApi
from airflow_client.client.api.monitoring_api import MonitoringApi
from airflow_client.client.api.permission_api import PermissionApi
from airflow_client.client.api.plugin_api import PluginApi
from airflow_client.client.api.pool_api import PoolApi
from airflow_client.client.api.provider_api import ProviderApi
from airflow_client.client.api.role_api import RoleApi
from airflow_client.client.api.task_instance_api import TaskInstanceApi
from airflow_client.client.api.user_api import UserApi
from airflow_client.client.api.variable_api import VariableApi
from airflow_client.client.api.x_com_api import XComApi
