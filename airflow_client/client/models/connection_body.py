# coding: utf-8

"""
    Airflow API

    Airflow API. All endpoints located under ``/api/v2`` can be used safely, are stable and backward compatible. Endpoints located under ``/ui`` are dedicated to the UI and are subject to breaking change depending on the need of the frontend. Users should not rely on those but use the public ones instead.

    The version of the OpenAPI document: 2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class ConnectionBody(BaseModel):
    """
    Connection Serializer for requests body.
    """ # noqa: E501
    conn_type: StrictStr
    connection_id: Annotated[str, Field(strict=True, max_length=200)]
    description: Optional[StrictStr] = None
    extra: Optional[StrictStr] = None
    host: Optional[StrictStr] = None
    login: Optional[StrictStr] = None
    password: Optional[StrictStr] = None
    port: Optional[StrictInt] = None
    var_schema: Optional[StrictStr] = Field(default=None, alias="schema")
    __properties: ClassVar[List[str]] = ["conn_type", "connection_id", "description", "extra", "host", "login", "password", "port", "schema"]

    @field_validator('connection_id')
    def connection_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[\w.-]+$", value):
            raise ValueError(r"must validate the regular expression /^[\w.-]+$/")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ConnectionBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConnectionBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "conn_type": obj.get("conn_type"),
            "connection_id": obj.get("connection_id"),
            "description": obj.get("description"),
            "extra": obj.get("extra"),
            "host": obj.get("host"),
            "login": obj.get("login"),
            "password": obj.get("password"),
            "port": obj.get("port"),
            "schema": obj.get("schema")
        })
        return _obj


