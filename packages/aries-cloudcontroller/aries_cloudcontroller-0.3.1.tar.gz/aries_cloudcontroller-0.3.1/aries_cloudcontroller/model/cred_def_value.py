# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.cred_def_value_primary import CredDefValuePrimary
from aries_cloudcontroller.model.cred_def_value_revocation import CredDefValueRevocation


class CredDefValue(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CredDefValue - a model defined in OpenAPI
        primary: Primary value for credential definition [Optional].
        revocation: Revocation value for credential definition [Optional].
    """

    primary: Optional[CredDefValuePrimary] = None
    revocation: Optional[CredDefValueRevocation] = None

    def __init__(
        self,
        *,
        primary: Optional[CredDefValuePrimary] = None,
        revocation: Optional[CredDefValueRevocation] = None,
        **kwargs,
    ):
        super().__init__(
            primary=primary,
            revocation=revocation,
            **kwargs,
        )

    class Config:
        allow_population_by_field_name = True


CredDefValue.update_forward_refs()
