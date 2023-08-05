# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.model_schema import ModelSchema


class SchemaGetResult(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SchemaGetResult - a model defined in OpenAPI
        schema_: The schema_ of this SchemaGetResult [Optional].
    """

    schema_: Optional[ModelSchema] = Field(None, alias="schema")

    def __init__(
        self,
        *,
        schema_: Optional[ModelSchema] = None,
        **kwargs,
    ):
        super().__init__(
            schema_=schema_,
            **kwargs,
        )

    class Config:
        allow_population_by_field_name = True


SchemaGetResult.update_forward_refs()
