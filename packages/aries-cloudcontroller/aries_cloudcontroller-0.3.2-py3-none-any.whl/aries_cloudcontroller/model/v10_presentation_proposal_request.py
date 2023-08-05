# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.indy_pres_preview import IndyPresPreview


class V10PresentationProposalRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V10PresentationProposalRequest - a model defined in OpenAPI
        connection_id: Connection identifier.
        presentation_proposal: The presentation_proposal of this V10PresentationProposalRequest.
        auto_present: Whether to respond automatically to presentation requests, building and presenting requested proof [Optional].
        comment: Human-readable comment [Optional].
        trace: Whether to trace event (default false) [Optional].
    """

    connection_id: str
    presentation_proposal: IndyPresPreview
    auto_present: Optional[bool] = None
    comment: Optional[str] = None
    trace: Optional[bool] = None

    def __init__(
        self,
        *,
        connection_id: str = None,
        presentation_proposal: IndyPresPreview = None,
        auto_present: Optional[bool] = None,
        comment: Optional[str] = None,
        trace: Optional[bool] = None,
        **kwargs,
    ):
        super().__init__(
            auto_present=auto_present,
            comment=comment,
            connection_id=connection_id,
            presentation_proposal=presentation_proposal,
            trace=trace,
            **kwargs,
        )

    class Config:
        allow_population_by_field_name = True


V10PresentationProposalRequest.update_forward_refs()
