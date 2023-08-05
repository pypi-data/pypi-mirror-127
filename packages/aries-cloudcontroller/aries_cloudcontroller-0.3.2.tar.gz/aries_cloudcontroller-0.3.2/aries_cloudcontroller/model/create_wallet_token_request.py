# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class CreateWalletTokenRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CreateWalletTokenRequest - a model defined in OpenAPI
        wallet_key: Master key used for key derivation. Only required for             unamanged wallets. [Optional].
    """

    wallet_key: Optional[str] = None

    def __init__(
        self,
        *,
        wallet_key: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            wallet_key=wallet_key,
            **kwargs,
        )

    class Config:
        allow_population_by_field_name = True


CreateWalletTokenRequest.update_forward_refs()
