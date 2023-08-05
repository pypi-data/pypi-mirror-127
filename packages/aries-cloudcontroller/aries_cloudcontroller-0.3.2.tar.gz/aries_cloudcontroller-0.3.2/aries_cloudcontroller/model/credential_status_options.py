# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class CredentialStatusOptions(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CredentialStatusOptions - a model defined in OpenAPI
        type: Credential status method type to use for the credential. Should match status method registered in the Verifiable Credential Extension Registry.
    """

    type: str

    def __init__(
        self,
        *,
        type: str = None,
        **kwargs,
    ):
        super().__init__(
            type=type,
            **kwargs,
        )

    class Config:
        allow_population_by_field_name = True


CredentialStatusOptions.update_forward_refs()
