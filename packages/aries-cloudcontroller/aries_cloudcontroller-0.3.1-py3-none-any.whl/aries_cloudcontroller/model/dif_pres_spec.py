# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.presentation_definition import PresentationDefinition


class DIFPresSpec(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    DIFPresSpec - a model defined in OpenAPI
        issuer_id: Issuer identifier to sign the presentation, if different from current public DID [Optional].
        presentation_definition: The presentation_definition of this DIFPresSpec [Optional].
        record_ids: Mapping of input_descriptor id to list of stored W3C credential record_id [Optional].
    """

    issuer_id: Optional[str] = None
    presentation_definition: Optional[PresentationDefinition] = None
    record_ids: Optional[Dict[str, Any]] = None

    def __init__(
        self,
        *,
        issuer_id: Optional[str] = None,
        presentation_definition: Optional[PresentationDefinition] = None,
        record_ids: Optional[Dict[str, Any]] = None,
        **kwargs,
    ):
        super().__init__(
            issuer_id=issuer_id,
            presentation_definition=presentation_definition,
            record_ids=record_ids,
            **kwargs,
        )

    class Config:
        allow_population_by_field_name = True


DIFPresSpec.update_forward_refs()
