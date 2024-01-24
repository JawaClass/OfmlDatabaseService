import Service.tables.go as go
import Service.tables.ocd as ocd
import Service.tables.oas as oas
import Service.tables.oam as oam
import Service.tables.oap as oap
import Service.tables.odb as odb
# from copy import copy
import inspect

_modules = [go, ocd, oam, oap, oas, odb]


def get_classes(module):
    classes = []
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            classes.append(obj)
    return classes


TABLE_NAME_2_CLASS = {}
_classes_ = [cls for module in _modules for cls in get_classes(module)]

for class_ in _classes_:
    if hasattr(class_, "__tablename__"):
        table_name = getattr(class_, "__tablename__")
        TABLE_NAME_2_CLASS[table_name] = class_

# print("TABLE_NAME_2_CLASS")
# for i, (k, v) in enumerate(TABLE_NAME_2_CLASS.items()):
#     print(f"{i}::", k, v)
