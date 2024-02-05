import os
from pathlib import Path


class Config:

    CREATE_OFML_EXPORT_PATH = os.environ.get("CREATE_OFML_EXPORT_PATH", None)#r"\\w2_fs1\edv\knps-testumgebung\ofml_development\Tools\ofml_datenmacher" #"B:\ofml_development\Tools\ofml_datenmacher" # os.environ.get("CREATE_OFML_EXPORT_PATH") # "B:\ofml_development\Tools\ofml_datenmacher"
    SECRET_KEY = "dev",
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:@172.22.253.244/ofml"
    IMPORT_PLAINTEXT_PATH = os.environ.get("IMPORT_PLAINTEXT_PATH", None)


assert Config.CREATE_OFML_EXPORT_PATH is not None and Path(Config.CREATE_OFML_EXPORT_PATH).exists()
assert Config.IMPORT_PLAINTEXT_PATH is not None and Path(Config.IMPORT_PLAINTEXT_PATH).exists()
print("Config.IMPORT_PLAINTEXT_PATH", Config.IMPORT_PLAINTEXT_PATH)
print("Config.CREATE_OFML_EXPORT_PATH", Config.CREATE_OFML_EXPORT_PATH)

# $env:CREATE_OFML_EXPORT_Pprint("Config.CREATE_OFML_EXPORT_PATH", Config.CREATE_OFML_EXPORT_PATH)ATH = "B:\ofml_development\Tools\ofml_datenmacher"