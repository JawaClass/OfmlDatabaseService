import Service.tables.go as go
import Service.tables.ocd as ocd
import Service.tables.oas as oas
import Service.tables.oam as oam
import Service.tables.oap as oap
import Service.tables.odb as odb
import Service.tables.web.ocd as web_ocd
import inspect

_modules = [go, ocd, oam, oap, oas, odb, web_ocd]


def get_classes(module):
    classes = []
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            classes.append(obj)
    return classes


def get_model_class_by_table_name(name: str):
    return _table_name_2_class[name]


_table_name_2_class = {}
_classes_ = [cls for module in _modules for cls in get_classes(module)]

for class_ in _classes_:
    if hasattr(class_, "__tablename__"):
        table_name = getattr(class_, "__tablename__")
        _table_name_2_class[table_name] = class_

# print("TABLE_NAME_2_CLASS")
# for i, (k, v) in enumerate(TABLE_NAME_2_CLASS.items()):
#     print(f"{i}::", k, v)
