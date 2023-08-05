# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.keylist_update_rule import KeylistUpdateRule


class KeylistUpdate(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    KeylistUpdate - a model defined in OpenAPI
        id: Message identifier [Optional].
        type: Message type [Optional].
        updates: List of update rules [Optional].
    """

    id: Optional[str] = Field(None, alias="@id")
    type: Optional[str] = Field(None, alias="@type")
    updates: Optional[List[KeylistUpdateRule]] = None

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        type: Optional[str] = None,
        updates: Optional[List[KeylistUpdateRule]] = None,
        **kwargs,
    ):
        super().__init__(
            id=id,
            type=type,
            updates=updates,
            **kwargs,
        )

    class Config:
        allow_population_by_field_name = True


KeylistUpdate.update_forward_refs()
