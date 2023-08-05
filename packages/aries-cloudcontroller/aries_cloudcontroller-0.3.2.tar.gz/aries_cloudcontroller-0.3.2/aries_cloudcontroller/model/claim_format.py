# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class ClaimFormat(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ClaimFormat - a model defined in OpenAPI
        jwt: The jwt of this ClaimFormat [Optional].
        jwt_vc: The jwt_vc of this ClaimFormat [Optional].
        jwt_vp: The jwt_vp of this ClaimFormat [Optional].
        ldp: The ldp of this ClaimFormat [Optional].
        ldp_vc: The ldp_vc of this ClaimFormat [Optional].
        ldp_vp: The ldp_vp of this ClaimFormat [Optional].
    """

    jwt: Optional[Dict[str, Any]] = None
    jwt_vc: Optional[Dict[str, Any]] = None
    jwt_vp: Optional[Dict[str, Any]] = None
    ldp: Optional[Dict[str, Any]] = None
    ldp_vc: Optional[Dict[str, Any]] = None
    ldp_vp: Optional[Dict[str, Any]] = None

    def __init__(
        self,
        *,
        jwt: Optional[Dict[str, Any]] = None,
        jwt_vc: Optional[Dict[str, Any]] = None,
        jwt_vp: Optional[Dict[str, Any]] = None,
        ldp: Optional[Dict[str, Any]] = None,
        ldp_vc: Optional[Dict[str, Any]] = None,
        ldp_vp: Optional[Dict[str, Any]] = None,
        **kwargs,
    ):
        super().__init__(
            jwt=jwt,
            jwt_vc=jwt_vc,
            jwt_vp=jwt_vp,
            ldp=ldp,
            ldp_vc=ldp_vc,
            ldp_vp=ldp_vp,
            **kwargs,
        )

    class Config:
        allow_population_by_field_name = True


ClaimFormat.update_forward_refs()
