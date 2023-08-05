# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class CredAttrSpec(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CredAttrSpec - a model defined in OpenAPI
        name: Attribute name.
        value: Attribute value: base64-encode if MIME type is present.
        mime_type: MIME type: omit for (null) default [Optional].
    """

    name: str
    value: str
    mime_type: Optional[str] = Field(None, alias="mime-type")

    def __init__(
        self,
        *,
        name: str = None,
        value: str = None,
        mime_type: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            mime_type=mime_type,
            name=name,
            value=value,
            **kwargs,
        )

    class Config:
        allow_population_by_field_name = True


CredAttrSpec.update_forward_refs()
