# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class SignatureOptions(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SignatureOptions - a model defined in OpenAPI
        proof_purpose: The proof_purpose of this SignatureOptions.
        verification_method: The verification_method of this SignatureOptions.
        challenge: The challenge of this SignatureOptions [Optional].
        domain: The domain of this SignatureOptions [Optional].
        type: The type of this SignatureOptions [Optional].
    """

    proof_purpose: str = Field(..., alias="proofPurpose")
    verification_method: str = Field(..., alias="verificationMethod")
    challenge: Optional[str] = None
    domain: Optional[str] = None
    type: Optional[str] = None

    def __init__(
        self,
        *,
        proof_purpose: str = None,
        verification_method: str = None,
        challenge: Optional[str] = None,
        domain: Optional[str] = None,
        type: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            challenge=challenge,
            domain=domain,
            proof_purpose=proof_purpose,
            type=type,
            verification_method=verification_method,
            **kwargs,
        )

    class Config:
        allow_population_by_field_name = True


SignatureOptions.update_forward_refs()
