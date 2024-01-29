from sqlalchemy import BigInteger, Column, Float, Index, Integer, SmallInteger, String, Text

from .. import db

Base = db.Model


def to_json(self):
    """
    returns a ordered json/dict of class by class attribute order
    """
    json = {}
    ordered_values = self.__class__.__dict__
    attributes = self.__dict__
    for k in ordered_values:
        if k in attributes and not k.startswith("_"):
            json[k] = attributes[k]
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
