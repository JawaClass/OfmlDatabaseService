import os


class Config:

    CREATE_OFML_EXPORT_PATH = "B:\ofml_development\Tools\ofml_datenmacher" # os.environ.get("CREATE_OFML_EXPORT_PATH") # "B:\ofml_development\Tools\ofml_datenmacher"
    SECRET_KEY = "dev",
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:@pdf2obs01/ofml"


assert Config.CREATE_OFML_EXPORT_PATH is not None
print("Config.CREATE_OFML_EXPORT_PATH", Config.CREATE_OFML_EXPORT_PATH)

# $env:CREATE_OFML_EXPORT_PATH = "B:\ofml_development\Tools\ofml_datenmacher"