# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import pydantic_v1


class ClassifySessionRequest(pydantic_v1.BaseModel):
    classes: typing.List[str] = pydantic_v1.Field()
    """
    The classes to use for classification.
    """

    instruction: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Custom instruction to use for classification.
    """

    last_n: typing.Optional[int] = pydantic_v1.Field(default=None)
    """
    The number of session messages to consider for classification. Defaults to 4.
    """

    name: str = pydantic_v1.Field()
    """
    The name of the classifier. Will be used to store the classification in session metadata if persist is True.
    """

    persist: typing.Optional[bool] = pydantic_v1.Field(default=None)
    """
    Whether to persist the classification to session metadata. Defaults to True.
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
