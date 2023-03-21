import re
from datetime import datetime, timezone
from typing import Any, Dict, Optional, Pattern

import pytz

from dateutil import parser
from pydantic import ConstrainedStr, errors
from pydantic.types import OptionalInt
from pydantic.utils import update_not_none
from pydantic.validators import (
    constr_length_validator,
    constr_lower,
    constr_strip_whitespace,
    str_validator,
    strict_str_validator,
)


def constr_null_char(v: str, field, config):
    return str(v).replace("\x00", "")


class FormattedDatetime(ConstrainedStr):
    regex = re.compile(r"(\d{2})\.(\d{2})\.(\d{4}) (\d{2}):(\d{2}):(\d{2})")


class ValidDateTime(datetime):
    """
    Формат datetime, часовой пояс которого может быть только UTC, при подаче другого
    часового пояса конвертирует в UTC
    """

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(
            examples=["2000-01-01T00:00:00+10:00", "2000-01-01T00:00:00-5:00"],
        )

    @classmethod
    def _from(cls, dt: datetime):
        return cls(
            year=dt.year,
            month=dt.month,
            day=dt.day,
            hour=dt.hour,
            minute=dt.minute,
            second=dt.second,
            microsecond=dt.microsecond,
            tzinfo=dt.tzinfo,
        )

    @classmethod
    def convert(cls, dt: datetime):
        if dt.tzinfo == pytz.utc:
            return cls._from(dt)
        if dt.tzinfo is not None:
            return cls._from(dt.astimezone(timezone.utc))
        else:
            return cls._from(pytz.utc.localize(dt))

    @classmethod
    def formatted(cls, dt: datetime):
        return FormattedDatetime(cls.convert(dt).strftime("%d.%m.%Y %H:%M:%S"))

    @classmethod
    def validate(cls, value: str | datetime):
        match value:
            case str():
                dt = parser.parse(value)
            case datetime():
                dt = value
            case _:
                raise TypeError("Value must be str or datetime instance")

        return cls.convert(dt)


class ValidatedString(str):
    strip_whitespace = False
    to_lower = False
    min_length: OptionalInt = None
    max_length: OptionalInt = None
    curtail_length: OptionalInt = None
    regex: Optional[Pattern[str]] = None
    strict = False

    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None:
        update_not_none(
            field_schema,
            minLength=cls.min_length,
            maxLength=cls.max_length,
            pattern=cls.regex and cls.regex.pattern,
        )

    @classmethod
    def __get_validators__(cls):
        yield constr_null_char
        yield strict_str_validator if cls.strict else str_validator
        yield constr_strip_whitespace
        yield constr_lower
        yield constr_length_validator
        yield cls.validate

    @classmethod
    def validate(cls, value: str) -> str:
        if cls.curtail_length and len(value) > cls.curtail_length:
            value = value[: cls.curtail_length]

        if cls.regex:
            if not cls.regex.match(value):
                raise errors.StrRegexError(pattern=cls.regex.pattern)

        return value
