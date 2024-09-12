# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .apidata_session_fact_rating_examples import ApidataSessionFactRatingExamples


class ApidataSessionFactRatingInstruction(pydantic_v1.BaseModel):
    examples: typing.Optional[ApidataSessionFactRatingExamples] = pydantic_v1.Field(default=None)
    """
    Examples is a list of examples that demonstrate how facts might be rated based on your instruction. You should provide
    an example of a highly rated example, a low rated example, and a medium (or in between example). For example, if you are rating
    based on relevance to a trip planning application, your examples might be:
    High: "Joe's dream vacation is Bali"
    Medium: "Joe has a fear of flying",
    Low: "Joe's favorite food is Japanese",
    """

    instruction: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    A string describing how to rate facts as they apply to your application. A trip planning application may
    use something like "relevancy to planning a trip, the user's preferences when traveling,
    or the user's travel history."
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
