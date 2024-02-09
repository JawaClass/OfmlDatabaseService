from pathlib import Path

from Service.api.export_program import Tables


class CreateInterface:
    path: Path
    tables: Tables

    def load(self):  ...

    def update(self):  ...

    def export(self):  ...

    def build_ebase(self): ...
