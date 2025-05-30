# coding: utf-8

"""
    Airflow API

    Airflow API. All endpoints located under ``/api/v2`` can be used safely, are stable and backward compatible. Endpoints located under ``/ui`` are dedicated to the UI and are subject to breaking change depending on the need of the frontend. Users should not rely on those but use the public ones instead.

    The version of the OpenAPI document: 2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from datetime import datetime
from pydantic import Field, StrictInt, StrictStr
from typing import List, Optional
from typing_extensions import Annotated
from airflow_client.client.models.event_log_collection_response import EventLogCollectionResponse
from airflow_client.client.models.event_log_response import EventLogResponse

from airflow_client.client.api_client import ApiClient, RequestSerialized
from airflow_client.client.api_response import ApiResponse
from airflow_client.client.rest import RESTResponseType


class EventLogApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def get_event_log(
        self,
        event_log_id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> EventLogResponse:
        """Get Event Log


        :param event_log_id: (required)
        :type event_log_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_event_log_serialize(
            event_log_id=event_log_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "EventLogResponse",
            '401': "HTTPExceptionResponse",
            '403': "HTTPExceptionResponse",
            '404': "HTTPExceptionResponse",
            '422': "HTTPValidationError",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_event_log_with_http_info(
        self,
        event_log_id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[EventLogResponse]:
        """Get Event Log


        :param event_log_id: (required)
        :type event_log_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_event_log_serialize(
            event_log_id=event_log_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "EventLogResponse",
            '401': "HTTPExceptionResponse",
            '403': "HTTPExceptionResponse",
            '404': "HTTPExceptionResponse",
            '422': "HTTPValidationError",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_event_log_without_preload_content(
        self,
        event_log_id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get Event Log


        :param event_log_id: (required)
        :type event_log_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_event_log_serialize(
            event_log_id=event_log_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "EventLogResponse",
            '401': "HTTPExceptionResponse",
            '403': "HTTPExceptionResponse",
            '404': "HTTPExceptionResponse",
            '422': "HTTPValidationError",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_event_log_serialize(
        self,
        event_log_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if event_log_id is not None:
            _path_params['event_log_id'] = event_log_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'OAuth2PasswordBearer'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v2/eventLogs/{event_log_id}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def get_event_logs(
        self,
        limit: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        order_by: Optional[StrictStr] = None,
        dag_id: Optional[StrictStr] = None,
        task_id: Optional[StrictStr] = None,
        run_id: Optional[StrictStr] = None,
        map_index: Optional[StrictInt] = None,
        try_number: Optional[StrictInt] = None,
        owner: Optional[StrictStr] = None,
        event: Optional[StrictStr] = None,
        excluded_events: Optional[List[StrictStr]] = None,
        included_events: Optional[List[StrictStr]] = None,
        before: Optional[datetime] = None,
        after: Optional[datetime] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> EventLogCollectionResponse:
        """Get Event Logs

        Get all Event Logs.

        :param limit:
        :type limit: int
        :param offset:
        :type offset: int
        :param order_by:
        :type order_by: str
        :param dag_id:
        :type dag_id: str
        :param task_id:
        :type task_id: str
        :param run_id:
        :type run_id: str
        :param map_index:
        :type map_index: int
        :param try_number:
        :type try_number: int
        :param owner:
        :type owner: str
        :param event:
        :type event: str
        :param excluded_events:
        :type excluded_events: List[str]
        :param included_events:
        :type included_events: List[str]
        :param before:
        :type before: datetime
        :param after:
        :type after: datetime
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_event_logs_serialize(
            limit=limit,
            offset=offset,
            order_by=order_by,
            dag_id=dag_id,
            task_id=task_id,
            run_id=run_id,
            map_index=map_index,
            try_number=try_number,
            owner=owner,
            event=event,
            excluded_events=excluded_events,
            included_events=included_events,
            before=before,
            after=after,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "EventLogCollectionResponse",
            '401': "HTTPExceptionResponse",
            '403': "HTTPExceptionResponse",
            '422': "HTTPValidationError",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_event_logs_with_http_info(
        self,
        limit: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        order_by: Optional[StrictStr] = None,
        dag_id: Optional[StrictStr] = None,
        task_id: Optional[StrictStr] = None,
        run_id: Optional[StrictStr] = None,
        map_index: Optional[StrictInt] = None,
        try_number: Optional[StrictInt] = None,
        owner: Optional[StrictStr] = None,
        event: Optional[StrictStr] = None,
        excluded_events: Optional[List[StrictStr]] = None,
        included_events: Optional[List[StrictStr]] = None,
        before: Optional[datetime] = None,
        after: Optional[datetime] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[EventLogCollectionResponse]:
        """Get Event Logs

        Get all Event Logs.

        :param limit:
        :type limit: int
        :param offset:
        :type offset: int
        :param order_by:
        :type order_by: str
        :param dag_id:
        :type dag_id: str
        :param task_id:
        :type task_id: str
        :param run_id:
        :type run_id: str
        :param map_index:
        :type map_index: int
        :param try_number:
        :type try_number: int
        :param owner:
        :type owner: str
        :param event:
        :type event: str
        :param excluded_events:
        :type excluded_events: List[str]
        :param included_events:
        :type included_events: List[str]
        :param before:
        :type before: datetime
        :param after:
        :type after: datetime
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_event_logs_serialize(
            limit=limit,
            offset=offset,
            order_by=order_by,
            dag_id=dag_id,
            task_id=task_id,
            run_id=run_id,
            map_index=map_index,
            try_number=try_number,
            owner=owner,
            event=event,
            excluded_events=excluded_events,
            included_events=included_events,
            before=before,
            after=after,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "EventLogCollectionResponse",
            '401': "HTTPExceptionResponse",
            '403': "HTTPExceptionResponse",
            '422': "HTTPValidationError",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_event_logs_without_preload_content(
        self,
        limit: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        order_by: Optional[StrictStr] = None,
        dag_id: Optional[StrictStr] = None,
        task_id: Optional[StrictStr] = None,
        run_id: Optional[StrictStr] = None,
        map_index: Optional[StrictInt] = None,
        try_number: Optional[StrictInt] = None,
        owner: Optional[StrictStr] = None,
        event: Optional[StrictStr] = None,
        excluded_events: Optional[List[StrictStr]] = None,
        included_events: Optional[List[StrictStr]] = None,
        before: Optional[datetime] = None,
        after: Optional[datetime] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get Event Logs

        Get all Event Logs.

        :param limit:
        :type limit: int
        :param offset:
        :type offset: int
        :param order_by:
        :type order_by: str
        :param dag_id:
        :type dag_id: str
        :param task_id:
        :type task_id: str
        :param run_id:
        :type run_id: str
        :param map_index:
        :type map_index: int
        :param try_number:
        :type try_number: int
        :param owner:
        :type owner: str
        :param event:
        :type event: str
        :param excluded_events:
        :type excluded_events: List[str]
        :param included_events:
        :type included_events: List[str]
        :param before:
        :type before: datetime
        :param after:
        :type after: datetime
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_event_logs_serialize(
            limit=limit,
            offset=offset,
            order_by=order_by,
            dag_id=dag_id,
            task_id=task_id,
            run_id=run_id,
            map_index=map_index,
            try_number=try_number,
            owner=owner,
            event=event,
            excluded_events=excluded_events,
            included_events=included_events,
            before=before,
            after=after,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "EventLogCollectionResponse",
            '401': "HTTPExceptionResponse",
            '403': "HTTPExceptionResponse",
            '422': "HTTPValidationError",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_event_logs_serialize(
        self,
        limit,
        offset,
        order_by,
        dag_id,
        task_id,
        run_id,
        map_index,
        try_number,
        owner,
        event,
        excluded_events,
        included_events,
        before,
        after,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'excluded_events': 'multi',
            'included_events': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        if offset is not None:
            
            _query_params.append(('offset', offset))
            
        if order_by is not None:
            
            _query_params.append(('order_by', order_by))
            
        if dag_id is not None:
            
            _query_params.append(('dag_id', dag_id))
            
        if task_id is not None:
            
            _query_params.append(('task_id', task_id))
            
        if run_id is not None:
            
            _query_params.append(('run_id', run_id))
            
        if map_index is not None:
            
            _query_params.append(('map_index', map_index))
            
        if try_number is not None:
            
            _query_params.append(('try_number', try_number))
            
        if owner is not None:
            
            _query_params.append(('owner', owner))
            
        if event is not None:
            
            _query_params.append(('event', event))
            
        if excluded_events is not None:
            
            _query_params.append(('excluded_events', excluded_events))
            
        if included_events is not None:
            
            _query_params.append(('included_events', included_events))
            
        if before is not None:
            if isinstance(before, datetime):
                _query_params.append(
                    (
                        'before',
                        before.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('before', before))
            
        if after is not None:
            if isinstance(after, datetime):
                _query_params.append(
                    (
                        'after',
                        after.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('after', after))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'OAuth2PasswordBearer'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v2/eventLogs',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


