import Service.tables.go as go
import Service.tables.ocd as ocd
import Service.tables.oas as oas
import Service.tables.oam as oam
import Service.tables.oap as oap
import Service.tables.odb as odb
import Service.tables.web.ocd as web_ocd
import inspect

from Service.api.web_ofml import models

_modules = [go, ocd, oam, oap, oas, odb, web_ocd, models]


def get_classes(module):
    classes = []
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            classes.append(obj)
    return classes


def get_model_class_by_table_name(name: str):
    return _table_name_2_class[name]


def get_table_classes_by_module_name(name: str):
    return _module_2_classes[name]


_module_2_classes = {}
_table_name_2_class = {}
for module_ in _modules:
    classes_ = get_classes(module_)
    _module_2_classes[module_.__name__] = classes_
    for class_ in classes_:
        if hasattr(class_, "__tablename__"):
            table_name = getattr(class_, "__tablename__")
            _table_name_2_class[table_name] = class_

