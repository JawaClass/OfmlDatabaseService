from Service.api.program_creation import Tables


class CreateInterface:

    tables: Tables

    def load(self):  ...

    def update(self):  ...

    def export(self):  ...
