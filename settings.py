import os
from pathlib import Path


class Config:

    CREATE_OFML_EXPORT_PATH = r"\\w2_fs1\edv\knps-testumgebung\ofml_development\Tools\ofml_datenmacher" #"B:\ofml_development\Tools\ofml_datenmacher" # os.environ.get("CREATE_OFML_EXPORT_PATH") # "B:\ofml_development\Tools\ofml_datenmacher"
    SECRET_KEY = "dev",
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:@pdf2obs01/ofml"


assert Config.CREATE_OFML_EXPORT_PATH is not None and Path(Config.CREATE_OFML_EXPORT_PATH).exists()
print("Config.CREATE_OFML_EXPORT_PATH", Config.CREATE_OFML_EXPORT_PATH)

# $env:CREATE_OFML_EXPORT_PATH = "B:\ofml_development\Tools\ofml_datenmacher"