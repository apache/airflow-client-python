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

    # Overview  To facilitate management, Apache Airflow supports a range of REST API endpoints across its objects. This section provides an overview of the API design, methods, and supported use cases.  Most of the endpoints accept `JSON` as input and return `JSON` responses. This means that you must usually add the following headers to your request: ``` Content-type: application/json Accept: application/json ```  ## Resources  The term `resource` refers to a single type of object in the Airflow metadata. An API is broken up by its endpoint's corresponding resource. The name of a resource is typically plural and expressed in camelCase. Example: `dagRuns`.  Resource names are used as part of endpoint URLs, as well as in API parameters and responses.  ## CRUD Operations  The platform supports **C**reate, **R**ead, **U**pdate, and **D**elete operations on most resources. You can review the standards for these operations and their standard parameters below.  Some endpoints have special behavior as exceptions.  ### Create  To create a resource, you typically submit an HTTP `POST` request with the resource's required metadata in the request body. The response returns a `201 Created` response code upon success with the resource's metadata, including its internal `id`, in the response body.  ### Read  The HTTP `GET` request can be used to read a resource or to list a number of resources.  A resource's `id` can be submitted in the request parameters to read a specific resource. The response usually returns a `200 OK` response code upon success, with the resource's metadata in the response body.  If a `GET` request does not include a specific resource `id`, it is treated as a list request. The response usually returns a `200 OK` response code upon success, with an object containing a list of resources' metadata in the response body.  When reading resources, some common query parameters are usually available. e.g.: ``` v1/connections?limit=25&offset=25 ```  |Query Parameter|Type|Description| |---------------|----|-----------| |limit|integer|Maximum number of objects to fetch. Usually 25 by default| |offset|integer|Offset after which to start returning objects. For use with limit query parameter.|  ### Update  Updating a resource requires the resource `id`, and is typically done using an HTTP `PATCH` request, with the fields to modify in the request body. The response usually returns a `200 OK` response code upon success, with information about the modified resource in the response body.  ### Delete  Deleting a resource requires the resource `id` and is typically executed via an HTTP `DELETE` request. The response usually returns a `204 No Content` response code upon success.  ## Conventions  - Resource names are plural and expressed in camelCase. - Names are consistent between URL parameter name and field name.  - Field names are in snake_case. ```json {     \"description\": \"string\",     \"name\": \"string\",     \"occupied_slots\": 0,     \"open_slots\": 0     \"queued_slots\": 0,     \"running_slots\": 0,     \"scheduled_slots\": 0,     \"slots\": 0, } ```  ### Update Mask  Update mask is available as a query parameter in patch endpoints. It is used to notify the API which fields you want to update. Using `update_mask` makes it easier to update objects by helping the server know which fields to update in an object instead of updating all fields. The update request ignores any fields that aren't specified in the field mask, leaving them with their current values.  Example: ```   resource = request.get('/resource/my-id').json()   resource['my_field'] = 'new-value'   request.patch('/resource/my-id?update_mask=my_field', data=json.dumps(resource)) ```  ## Versioning and Endpoint Lifecycle  - API versioning is not synchronized to specific releases of the Apache Airflow. - APIs are designed to be backward compatible. - Any changes to the API will first go through a deprecation phase.  # Trying the API  You can use a third party client, such as [curl](https://curl.haxx.se/), [HTTPie](https://httpie.org/), [Postman](https://www.postman.com/) or [the Insomnia rest client](https://insomnia.rest/) to test the Apache Airflow API.  Note that you will need to pass credentials data.  For e.g., here is how to pause a DAG with [curl](https://curl.haxx.se/), when basic authorization is used: ```bash curl -X PATCH 'https://example.com/api/v1/dags/{dag_id}?update_mask=is_paused' \\ -H 'Content-Type: application/json' \\ --user \"username:password\" \\ -d '{     \"is_paused\": true }' ```  Using a graphical tool such as [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/), it is possible to import the API specifications directly:  1. Download the API specification by clicking the **Download** button at the top of this document 2. Import the JSON specification in the graphical tool of your choice.   - In *Postman*, you can click the **import** button at the top   - With *Insomnia*, you can just drag-and-drop the file on the UI  Note that with *Postman*, you can also generate code snippets by selecting a request and clicking on the **Code** button.  ## Enabling CORS  [Cross-origin resource sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) is a browser security feature that restricts HTTP requests that are initiated from scripts running in the browser.  For details on enabling/configuring CORS, see [Enabling CORS](https://airflow.apache.org/docs/apache-airflow/stable/security/api.html).  # Authentication  To be able to meet the requirements of many organizations, Airflow supports many authentication methods, and it is even possible to add your own method.  If you want to check which auth backend is currently set, you can use `airflow config get-value api auth_backends` command as in the example below. ```bash $ airflow config get-value api auth_backends airflow.api.auth.backend.basic_auth ``` The default is to deny all requests.  For details on configuring the authentication, see [API Authorization](https://airflow.apache.org/docs/apache-airflow/stable/security/api.html).  # Errors  We follow the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs. As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.  ## Unauthenticated  This indicates that the request has not been applied because it lacks valid authentication credentials for the target resource. Please check that you have valid credentials.  ## PermissionDenied  This response means that the server understood the request but refuses to authorize it because it lacks sufficient rights to the resource. It happens when you do not have the necessary permission to execute the action you performed. You need to get the appropriate permissions in other to resolve this error.  ## BadRequest  This response means that the server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). To resolve this, please ensure that your syntax is correct.  ## NotFound  This client error response indicates that the server cannot find the requested resource.  ## MethodNotAllowed  Indicates that the request method is known by the server but is not supported by the target resource.  ## NotAcceptable  The target resource does not have a current representation that would be acceptable to the user agent, according to the proactive negotiation header fields received in the request, and the server is unwilling to supply a default representation.  ## AlreadyExists  The request could not be completed due to a conflict with the current state of the target resource, e.g. the resource it tries to create already exists.  ## Unknown  This means that the server encountered an unexpected condition that prevented it from fulfilling the request.   # noqa: E501

    The version of the OpenAPI document: 2.7.2
    Contact: dev@airflow.apache.org
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from airflow_client.client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from airflow_client.client.exceptions import ApiAttributeError


def lazy_import():
    from airflow_client.client.model.dag import DAG
    from airflow_client.client.model.dag_detail_all_of import DAGDetailAllOf
    from airflow_client.client.model.schedule_interval import ScheduleInterval
    from airflow_client.client.model.tag import Tag
    from airflow_client.client.model.time_delta import TimeDelta
    globals()['DAG'] = DAG
    globals()['DAGDetailAllOf'] = DAGDetailAllOf
    globals()['ScheduleInterval'] = ScheduleInterval
    globals()['Tag'] = Tag
    globals()['TimeDelta'] = TimeDelta


class DAGDetail(ModelComposed):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'dag_id': (str,),  # noqa: E501
            'root_dag_id': (str, none_type,),  # noqa: E501
            'is_paused': (bool, none_type,),  # noqa: E501
            'is_active': (bool, none_type,),  # noqa: E501
            'is_subdag': (bool,),  # noqa: E501
            'last_parsed_time': (datetime, none_type,),  # noqa: E501
            'last_pickled': (datetime, none_type,),  # noqa: E501
            'last_expired': (datetime, none_type,),  # noqa: E501
            'scheduler_lock': (bool, none_type,),  # noqa: E501
            'pickle_id': (str, none_type,),  # noqa: E501
            'default_view': (str,),  # noqa: E501
            'fileloc': (str,),  # noqa: E501
            'file_token': (str,),  # noqa: E501
            'owners': ([str],),  # noqa: E501
            'description': (str, none_type,),  # noqa: E501
            'schedule_interval': (ScheduleInterval,),  # noqa: E501
            'timetable_description': (str, none_type,),  # noqa: E501
            'tags': ([Tag], none_type,),  # noqa: E501
            'max_active_tasks': (int, none_type,),  # noqa: E501
            'max_active_runs': (int, none_type,),  # noqa: E501
            'has_task_concurrency_limits': (bool, none_type,),  # noqa: E501
            'has_import_errors': (bool, none_type,),  # noqa: E501
            'next_dagrun': (datetime, none_type,),  # noqa: E501
            'next_dagrun_data_interval_start': (datetime, none_type,),  # noqa: E501
            'next_dagrun_data_interval_end': (datetime, none_type,),  # noqa: E501
            'next_dagrun_create_after': (datetime, none_type,),  # noqa: E501
            'timezone': (str,),  # noqa: E501
            'catchup': (bool,),  # noqa: E501
            'orientation': (str,),  # noqa: E501
            'concurrency': (float,),  # noqa: E501
            'start_date': (datetime, none_type,),  # noqa: E501
            'dag_run_timeout': (TimeDelta,),  # noqa: E501
            'doc_md': (str, none_type,),  # noqa: E501
            'params': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'end_date': (datetime, none_type,),  # noqa: E501
            'is_paused_upon_creation': (bool, none_type,),  # noqa: E501
            'last_parsed': (datetime, none_type,),  # noqa: E501
            'template_search_path': ([str], none_type,),  # noqa: E501
            'render_template_as_native_obj': (bool, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'dag_id': 'dag_id',  # noqa: E501
        'root_dag_id': 'root_dag_id',  # noqa: E501
        'is_paused': 'is_paused',  # noqa: E501
        'is_active': 'is_active',  # noqa: E501
        'is_subdag': 'is_subdag',  # noqa: E501
        'last_parsed_time': 'last_parsed_time',  # noqa: E501
        'last_pickled': 'last_pickled',  # noqa: E501
        'last_expired': 'last_expired',  # noqa: E501
        'scheduler_lock': 'scheduler_lock',  # noqa: E501
        'pickle_id': 'pickle_id',  # noqa: E501
        'default_view': 'default_view',  # noqa: E501
        'fileloc': 'fileloc',  # noqa: E501
        'file_token': 'file_token',  # noqa: E501
        'owners': 'owners',  # noqa: E501
        'description': 'description',  # noqa: E501
        'schedule_interval': 'schedule_interval',  # noqa: E501
        'timetable_description': 'timetable_description',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        'max_active_tasks': 'max_active_tasks',  # noqa: E501
        'max_active_runs': 'max_active_runs',  # noqa: E501
        'has_task_concurrency_limits': 'has_task_concurrency_limits',  # noqa: E501
        'has_import_errors': 'has_import_errors',  # noqa: E501
        'next_dagrun': 'next_dagrun',  # noqa: E501
        'next_dagrun_data_interval_start': 'next_dagrun_data_interval_start',  # noqa: E501
        'next_dagrun_data_interval_end': 'next_dagrun_data_interval_end',  # noqa: E501
        'next_dagrun_create_after': 'next_dagrun_create_after',  # noqa: E501
        'timezone': 'timezone',  # noqa: E501
        'catchup': 'catchup',  # noqa: E501
        'orientation': 'orientation',  # noqa: E501
        'concurrency': 'concurrency',  # noqa: E501
        'start_date': 'start_date',  # noqa: E501
        'dag_run_timeout': 'dag_run_timeout',  # noqa: E501
        'doc_md': 'doc_md',  # noqa: E501
        'params': 'params',  # noqa: E501
        'end_date': 'end_date',  # noqa: E501
        'is_paused_upon_creation': 'is_paused_upon_creation',  # noqa: E501
        'last_parsed': 'last_parsed',  # noqa: E501
        'template_search_path': 'template_search_path',  # noqa: E501
        'render_template_as_native_obj': 'render_template_as_native_obj',  # noqa: E501
    }

    read_only_vars = {
        'dag_id',  # noqa: E501
        'root_dag_id',  # noqa: E501
        'is_active',  # noqa: E501
        'is_subdag',  # noqa: E501
        'last_parsed_time',  # noqa: E501
        'last_pickled',  # noqa: E501
        'last_expired',  # noqa: E501
        'scheduler_lock',  # noqa: E501
        'pickle_id',  # noqa: E501
        'default_view',  # noqa: E501
        'fileloc',  # noqa: E501
        'file_token',  # noqa: E501
        'owners',  # noqa: E501
        'description',  # noqa: E501
        'timetable_description',  # noqa: E501
        'tags',  # noqa: E501
        'max_active_tasks',  # noqa: E501
        'max_active_runs',  # noqa: E501
        'has_task_concurrency_limits',  # noqa: E501
        'has_import_errors',  # noqa: E501
        'next_dagrun',  # noqa: E501
        'next_dagrun_data_interval_start',  # noqa: E501
        'next_dagrun_data_interval_end',  # noqa: E501
        'next_dagrun_create_after',  # noqa: E501
        'catchup',  # noqa: E501
        'orientation',  # noqa: E501
        'concurrency',  # noqa: E501
        'start_date',  # noqa: E501
        'doc_md',  # noqa: E501
        'params',  # noqa: E501
        'end_date',  # noqa: E501
        'is_paused_upon_creation',  # noqa: E501
        'last_parsed',  # noqa: E501
        'render_template_as_native_obj',  # noqa: E501
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """DAGDetail - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            dag_id (str): The ID of the DAG.. [optional]  # noqa: E501
            root_dag_id (str, none_type): If the DAG is SubDAG then it is the top level DAG identifier. Otherwise, null.. [optional]  # noqa: E501
            is_paused (bool, none_type): Whether the DAG is paused.. [optional]  # noqa: E501
            is_active (bool, none_type): Whether the DAG is currently seen by the scheduler(s).  *New in version 2.1.1*  *Changed in version 2.2.0*&#58; Field is read-only. . [optional]  # noqa: E501
            is_subdag (bool): Whether the DAG is SubDAG.. [optional]  # noqa: E501
            last_parsed_time (datetime, none_type): The last time the DAG was parsed.  *New in version 2.3.0* . [optional]  # noqa: E501
            last_pickled (datetime, none_type): The last time the DAG was pickled.  *New in version 2.3.0* . [optional]  # noqa: E501
            last_expired (datetime, none_type): Time when the DAG last received a refresh signal (e.g. the DAG's \"refresh\" button was clicked in the web UI)  *New in version 2.3.0* . [optional]  # noqa: E501
            scheduler_lock (bool, none_type): Whether (one of) the scheduler is scheduling this DAG at the moment  *New in version 2.3.0* . [optional]  # noqa: E501
            pickle_id (str, none_type): Foreign key to the latest pickle_id  *New in version 2.3.0* . [optional]  # noqa: E501
            default_view (str): [optional]  # noqa: E501
            fileloc (str): The absolute path to the file.. [optional]  # noqa: E501
            file_token (str): The key containing the encrypted path to the file. Encryption and decryption take place only on the server. This prevents the client from reading an non-DAG file. This also ensures API extensibility, because the format of encrypted data may change. . [optional]  # noqa: E501
            owners ([str]): [optional]  # noqa: E501
            description (str, none_type): User-provided DAG description, which can consist of several sentences or paragraphs that describe DAG contents. . [optional]  # noqa: E501
            schedule_interval (ScheduleInterval): [optional]  # noqa: E501
            timetable_description (str, none_type): Timetable/Schedule Interval description.  *New in version 2.3.0* . [optional]  # noqa: E501
            tags ([Tag], none_type): List of tags.. [optional]  # noqa: E501
            max_active_tasks (int, none_type): Maximum number of active tasks that can be run on the DAG  *New in version 2.3.0* . [optional]  # noqa: E501
            max_active_runs (int, none_type): Maximum number of active DAG runs for the DAG  *New in version 2.3.0* . [optional]  # noqa: E501
            has_task_concurrency_limits (bool, none_type): Whether the DAG has task concurrency limits  *New in version 2.3.0* . [optional]  # noqa: E501
            has_import_errors (bool, none_type): Whether the DAG has import errors  *New in version 2.3.0* . [optional]  # noqa: E501
            next_dagrun (datetime, none_type): The logical date of the next dag run.  *New in version 2.3.0* . [optional]  # noqa: E501
            next_dagrun_data_interval_start (datetime, none_type): The start of the interval of the next dag run.  *New in version 2.3.0* . [optional]  # noqa: E501
            next_dagrun_data_interval_end (datetime, none_type): The end of the interval of the next dag run.  *New in version 2.3.0* . [optional]  # noqa: E501
            next_dagrun_create_after (datetime, none_type): Earliest time at which this ``next_dagrun`` can be created.  *New in version 2.3.0* . [optional]  # noqa: E501
            timezone (str): [optional]  # noqa: E501
            catchup (bool): [optional]  # noqa: E501
            orientation (str): [optional]  # noqa: E501
            concurrency (float): [optional]  # noqa: E501
            start_date (datetime, none_type): The DAG's start date.  *Changed in version 2.0.1*&#58; Field becomes nullable. . [optional]  # noqa: E501
            dag_run_timeout (TimeDelta): [optional]  # noqa: E501
            doc_md (str, none_type): [optional]  # noqa: E501
            params ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): User-specified DAG params.  *New in version 2.0.1* . [optional]  # noqa: E501
            end_date (datetime, none_type): The DAG's end date.  *New in version 2.3.0*. . [optional]  # noqa: E501
            is_paused_upon_creation (bool, none_type): Whether the DAG is paused upon creation.  *New in version 2.3.0* . [optional]  # noqa: E501
            last_parsed (datetime, none_type): The last time the DAG was parsed.  *New in version 2.3.0* . [optional]  # noqa: E501
            template_search_path ([str], none_type): The template search path.  *New in version 2.3.0* . [optional]  # noqa: E501
            render_template_as_native_obj (bool, none_type): Whether to render templates as native Python objects.  *New in version 2.3.0* . [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)

        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """DAGDetail - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            dag_id (str): The ID of the DAG.. [optional]  # noqa: E501
            root_dag_id (str, none_type): If the DAG is SubDAG then it is the top level DAG identifier. Otherwise, null.. [optional]  # noqa: E501
            is_paused (bool, none_type): Whether the DAG is paused.. [optional]  # noqa: E501
            is_active (bool, none_type): Whether the DAG is currently seen by the scheduler(s).  *New in version 2.1.1*  *Changed in version 2.2.0*&#58; Field is read-only. . [optional]  # noqa: E501
            is_subdag (bool): Whether the DAG is SubDAG.. [optional]  # noqa: E501
            last_parsed_time (datetime, none_type): The last time the DAG was parsed.  *New in version 2.3.0* . [optional]  # noqa: E501
            last_pickled (datetime, none_type): The last time the DAG was pickled.  *New in version 2.3.0* . [optional]  # noqa: E501
            last_expired (datetime, none_type): Time when the DAG last received a refresh signal (e.g. the DAG's \"refresh\" button was clicked in the web UI)  *New in version 2.3.0* . [optional]  # noqa: E501
            scheduler_lock (bool, none_type): Whether (one of) the scheduler is scheduling this DAG at the moment  *New in version 2.3.0* . [optional]  # noqa: E501
            pickle_id (str, none_type): Foreign key to the latest pickle_id  *New in version 2.3.0* . [optional]  # noqa: E501
            default_view (str): [optional]  # noqa: E501
            fileloc (str): The absolute path to the file.. [optional]  # noqa: E501
            file_token (str): The key containing the encrypted path to the file. Encryption and decryption take place only on the server. This prevents the client from reading an non-DAG file. This also ensures API extensibility, because the format of encrypted data may change. . [optional]  # noqa: E501
            owners ([str]): [optional]  # noqa: E501
            description (str, none_type): User-provided DAG description, which can consist of several sentences or paragraphs that describe DAG contents. . [optional]  # noqa: E501
            schedule_interval (ScheduleInterval): [optional]  # noqa: E501
            timetable_description (str, none_type): Timetable/Schedule Interval description.  *New in version 2.3.0* . [optional]  # noqa: E501
            tags ([Tag], none_type): List of tags.. [optional]  # noqa: E501
            max_active_tasks (int, none_type): Maximum number of active tasks that can be run on the DAG  *New in version 2.3.0* . [optional]  # noqa: E501
            max_active_runs (int, none_type): Maximum number of active DAG runs for the DAG  *New in version 2.3.0* . [optional]  # noqa: E501
            has_task_concurrency_limits (bool, none_type): Whether the DAG has task concurrency limits  *New in version 2.3.0* . [optional]  # noqa: E501
            has_import_errors (bool, none_type): Whether the DAG has import errors  *New in version 2.3.0* . [optional]  # noqa: E501
            next_dagrun (datetime, none_type): The logical date of the next dag run.  *New in version 2.3.0* . [optional]  # noqa: E501
            next_dagrun_data_interval_start (datetime, none_type): The start of the interval of the next dag run.  *New in version 2.3.0* . [optional]  # noqa: E501
            next_dagrun_data_interval_end (datetime, none_type): The end of the interval of the next dag run.  *New in version 2.3.0* . [optional]  # noqa: E501
            next_dagrun_create_after (datetime, none_type): Earliest time at which this ``next_dagrun`` can be created.  *New in version 2.3.0* . [optional]  # noqa: E501
            timezone (str): [optional]  # noqa: E501
            catchup (bool): [optional]  # noqa: E501
            orientation (str): [optional]  # noqa: E501
            concurrency (float): [optional]  # noqa: E501
            start_date (datetime, none_type): The DAG's start date.  *Changed in version 2.0.1*&#58; Field becomes nullable. . [optional]  # noqa: E501
            dag_run_timeout (TimeDelta): [optional]  # noqa: E501
            doc_md (str, none_type): [optional]  # noqa: E501
            params ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): User-specified DAG params.  *New in version 2.0.1* . [optional]  # noqa: E501
            end_date (datetime, none_type): The DAG's end date.  *New in version 2.3.0*. . [optional]  # noqa: E501
            is_paused_upon_creation (bool, none_type): Whether the DAG is paused upon creation.  *New in version 2.3.0* . [optional]  # noqa: E501
            last_parsed (datetime, none_type): The last time the DAG was parsed.  *New in version 2.3.0* . [optional]  # noqa: E501
            template_search_path ([str], none_type): The template search path.  *New in version 2.3.0* . [optional]  # noqa: E501
            render_template_as_native_obj (bool, none_type): Whether to render templates as native Python objects.  *New in version 2.3.0* . [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [
              DAG,
              DAGDetailAllOf,
          ],
          'oneOf': [
          ],
        }
