import os
from pathlib import Path

ENV = "W2_FS1_DRIVE_EDV"
_w2_fs1_edv = os.environ.get(ENV, None)
assert _w2_fs1_edv, f"ENV missing: {ENV}"
print("_w2_fs1_edv::", _w2_fs1_edv)
_w2_fs1 = Path(_w2_fs1_edv)
assert _w2_fs1.exists(), f"{_w2_fs1} does not exist."

_root_project_path = Path(os.path.dirname(os.path.abspath(__file__)))


class Config:

    W2_FS1_DRIVE = _w2_fs1
    SECRET_KEY = "dev",
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:@172.22.253.244/ofml"
    IMPORT_PLAINTEXT_PATH = _w2_fs1 / "knps-testumgebung" / "ofml_development" / "repository" / "kn"
    EXPORT_DATA_PATH_TEST_ENV = _w2_fs1/ "knps-testumgebung" / "Testumgebung" / "EasternGraphics" / "kn"
    EXPORT_DATA_PATH_DEFAULT = _w2_fs1 / "knps-testumgebung" / "ofml_development" / "Tools" / "ofml_datenmacher"
    ROOT_PROJECT_FOLDER = _root_project_path
    CREATE_EBASE_EXE = _root_project_path / "tools" / "ebmkdb.exe"


assert Config.W2_FS1_DRIVE is not None and Path(Config.W2_FS1_DRIVE).exists()
assert Config.IMPORT_PLAINTEXT_PATH is not None and Path(Config.IMPORT_PLAINTEXT_PATH).exists()
print("Config.W2_FS1_DRIVE", Config.W2_FS1_DRIVE)
print("Config.IMPORT_PLAINTEXT_PATH", Config.IMPORT_PLAINTEXT_PATH)
print("Config.EXPORT_DATA_PATH_TEST_ENV", Config.EXPORT_DATA_PATH_TEST_ENV)
print("Config.EXPORT_DATA_PATH_DEFAULT", Config.EXPORT_DATA_PATH_DEFAULT)
