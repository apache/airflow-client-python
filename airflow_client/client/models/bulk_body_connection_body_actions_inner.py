# coding: utf-8

"""
    Airflow API

    Airflow API. All endpoints located under ``/api/v2`` can be used safely, are stable and backward compatible. Endpoints located under ``/ui`` are dedicated to the UI and are subject to breaking change depending on the need of the frontend. Users should not rely on those but use the public ones instead.

    The version of the OpenAPI document: 2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from airflow_client.client.models.bulk_create_action_connection_body import BulkCreateActionConnectionBody
from airflow_client.client.models.bulk_delete_action_connection_body import BulkDeleteActionConnectionBody
from airflow_client.client.models.bulk_update_action_connection_body import BulkUpdateActionConnectionBody
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

BULKBODYCONNECTIONBODYACTIONSINNER_ONE_OF_SCHEMAS = ["BulkCreateActionConnectionBody", "BulkDeleteActionConnectionBody", "BulkUpdateActionConnectionBody"]

class BulkBodyConnectionBodyActionsInner(BaseModel):
    """
    BulkBodyConnectionBodyActionsInner
    """
    # data type: BulkCreateActionConnectionBody
    oneof_schema_1_validator: Optional[BulkCreateActionConnectionBody] = None
    # data type: BulkUpdateActionConnectionBody
    oneof_schema_2_validator: Optional[BulkUpdateActionConnectionBody] = None
    # data type: BulkDeleteActionConnectionBody
    oneof_schema_3_validator: Optional[BulkDeleteActionConnectionBody] = None
    actual_instance: Optional[Union[BulkCreateActionConnectionBody, BulkDeleteActionConnectionBody, BulkUpdateActionConnectionBody]] = None
    one_of_schemas: Set[str] = { "BulkCreateActionConnectionBody", "BulkDeleteActionConnectionBody", "BulkUpdateActionConnectionBody" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = BulkBodyConnectionBodyActionsInner.model_construct()
        error_messages = []
        match = 0
        # validate data type: BulkCreateActionConnectionBody
        if not isinstance(v, BulkCreateActionConnectionBody):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BulkCreateActionConnectionBody`")
        else:
            match += 1
        # validate data type: BulkUpdateActionConnectionBody
        if not isinstance(v, BulkUpdateActionConnectionBody):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BulkUpdateActionConnectionBody`")
        else:
            match += 1
        # validate data type: BulkDeleteActionConnectionBody
        if not isinstance(v, BulkDeleteActionConnectionBody):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BulkDeleteActionConnectionBody`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in BulkBodyConnectionBodyActionsInner with oneOf schemas: BulkCreateActionConnectionBody, BulkDeleteActionConnectionBody, BulkUpdateActionConnectionBody. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in BulkBodyConnectionBodyActionsInner with oneOf schemas: BulkCreateActionConnectionBody, BulkDeleteActionConnectionBody, BulkUpdateActionConnectionBody. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into BulkCreateActionConnectionBody
        try:
            instance.actual_instance = BulkCreateActionConnectionBody.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BulkUpdateActionConnectionBody
        try:
            instance.actual_instance = BulkUpdateActionConnectionBody.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BulkDeleteActionConnectionBody
        try:
            instance.actual_instance = BulkDeleteActionConnectionBody.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into BulkBodyConnectionBodyActionsInner with oneOf schemas: BulkCreateActionConnectionBody, BulkDeleteActionConnectionBody, BulkUpdateActionConnectionBody. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into BulkBodyConnectionBodyActionsInner with oneOf schemas: BulkCreateActionConnectionBody, BulkDeleteActionConnectionBody, BulkUpdateActionConnectionBody. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], BulkCreateActionConnectionBody, BulkDeleteActionConnectionBody, BulkUpdateActionConnectionBody]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


