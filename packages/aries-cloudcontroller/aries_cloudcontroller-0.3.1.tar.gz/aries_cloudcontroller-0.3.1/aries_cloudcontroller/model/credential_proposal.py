# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.credential_preview import CredentialPreview


class CredentialProposal(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CredentialProposal - a model defined in OpenAPI
        id: Message identifier [Optional].
        type: Message type [Optional].
        comment: Human-readable comment [Optional].
        cred_def_id: The cred_def_id of this CredentialProposal [Optional].
        credential_proposal: The credential_proposal of this CredentialProposal [Optional].
        issuer_did: The issuer_did of this CredentialProposal [Optional].
        schema_id: The schema_id of this CredentialProposal [Optional].
        schema_issuer_did: The schema_issuer_did of this CredentialProposal [Optional].
        schema_name: The schema_name of this CredentialProposal [Optional].
        schema_version: The schema_version of this CredentialProposal [Optional].
    """

    id: Optional[str] = Field(None, alias="@id")
    type: Optional[str] = Field(None, alias="@type")
    comment: Optional[str] = None
    cred_def_id: Optional[str] = None
    credential_proposal: Optional[CredentialPreview] = None
    issuer_did: Optional[str] = None
    schema_id: Optional[str] = None
    schema_issuer_did: Optional[str] = None
    schema_name: Optional[str] = None
    schema_version: Optional[str] = None

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        type: Optional[str] = None,
        comment: Optional[str] = None,
        cred_def_id: Optional[str] = None,
        credential_proposal: Optional[CredentialPreview] = None,
        issuer_did: Optional[str] = None,
        schema_id: Optional[str] = None,
        schema_issuer_did: Optional[str] = None,
        schema_name: Optional[str] = None,
        schema_version: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            id=id,
            type=type,
            comment=comment,
            cred_def_id=cred_def_id,
            credential_proposal=credential_proposal,
            issuer_did=issuer_did,
            schema_id=schema_id,
            schema_issuer_did=schema_issuer_did,
            schema_name=schema_name,
            schema_version=schema_version,
            **kwargs,
        )

    @validator("cred_def_id")
    def cred_def_id_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of cred_def_id does not match regex pattern ('{pattern}')"
            )
        return value

    @validator("issuer_did")
    def issuer_did_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of issuer_did does not match regex pattern ('{pattern}')"
            )
        return value

    @validator("schema_id")
    def schema_id_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of schema_id does not match regex pattern ('{pattern}')"
            )
        return value

    @validator("schema_issuer_did")
    def schema_issuer_did_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of schema_issuer_did does not match regex pattern ('{pattern}')"
            )
        return value

    @validator("schema_version")
    def schema_version_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^[0-9.]+$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of schema_version does not match regex pattern ('{pattern}')"
            )
        return value

    class Config:
        allow_population_by_field_name = True


CredentialProposal.update_forward_refs()
