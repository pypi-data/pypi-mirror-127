# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class SchemaSendRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SchemaSendRequest - a model defined in OpenAPI
        attributes: List of schema attributes.
        schema_name: Schema name.
        schema_version: Schema version.
    """

    attributes: List[str]
    schema_name: str
    schema_version: str

    def __init__(
        self,
        *,
        attributes: List[str] = None,
        schema_name: str = None,
        schema_version: str = None,
        **kwargs,
    ):
        super().__init__(
            attributes=attributes,
            schema_name=schema_name,
            schema_version=schema_version,
            **kwargs,
        )

    @validator("schema_version")
    def schema_version_pattern(cls, value):

        pattern = r"^[0-9.]+$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of schema_version does not match regex pattern ('{pattern}')"
            )
        return value

    class Config:
        allow_population_by_field_name = True


SchemaSendRequest.update_forward_refs()
