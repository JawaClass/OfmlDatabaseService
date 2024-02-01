from sqlalchemy import BigInteger, Column, Float, Index, Integer, SmallInteger, String, Text

from .. import db
from datetime import datetime
Base = db.Model


def _format_datetime(date: datetime):
    return {
        "year": date.year,
        "month": date.month,
        "day": date.day,
        "hour": date.hour,
        "minute": date.minute,
        "second": date.second,
    }


def to_json(self):
    """
    returns a ordered json/dict of class by class attribute order
    """
    print("to_json...")
    json = {}
    ordered_values = self.__class__.__dict__
    attributes = self.__dict__
    for k in ordered_values:
        if k in attributes and not k.startswith("_"):
            attribute = attributes[k]
            attribute_type = type(attribute)
            if attribute_type is datetime:
                attribute = _format_datetime(attribute)
            json[k] = attribute
            # print(k, attributes[k], type(attributes[k]), type(attributes[k]) is datetime)
    return json


class InstantiateFromJsonError(Exception):
    pass


def from_json(self, json):
    try:
        instance = self(**json)
        return instance
    except TypeError as e:
        raise InstantiateFromJsonError(f"""
Could not instantiate a instance of type {self}
 with arguments {json}.
 Check what arguments ít needs.
""") from e


def to_string(self):
    return f"DB_Model({type(self).__name__}) :: {to_json(self)}"


Base.from_json = lambda x, json: from_json(x, json)
Base.to_json = lambda x: to_json(x)
Base.__str__ = lambda x: to_string(x)
Base.__repr__ = Base.__str__
__all__ = ["BigInteger", "Column", "Float", "Index", "Integer", "SmallInteger", "String", "Text", "Base", "db"]
