import os
from pathlib import Path

ENV = "W2_FS1_DRIVE_KNPS_TESTUMGEBUNG"
_w2_fs1_knps_test_env = os.environ.get(ENV, None)
assert _w2_fs1_knps_test_env, f"ENV missing: {ENV}"
print("_w2_fs1_edv::", _w2_fs1_knps_test_env)
_w2_fs1_knps_test_env = Path(_w2_fs1_knps_test_env)
print(f"try connect to... {_w2_fs1_knps_test_env}")
assert _w2_fs1_knps_test_env.exists(), f"{_w2_fs1_knps_test_env} does not exist."

_root_project_path = Path(os.path.dirname(os.path.abspath(__file__)))


def get_os_type_name():
    import platform
    system = platform.system()
    if system.lower() == "windows":
        return "windows"
    return "linux"


class Config:
    OS_NAME = get_os_type_name()
    W2_FS1_KNPS_TEST_ENV = _w2_fs1_knps_test_env
    SECRET_KEY = "dev",
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:@172.22.253.244/ofml"
    IMPORT_PLAINTEXT_PATH = _w2_fs1_knps_test_env / "ofml_development" / "repository" / "kn"
    EXPORT_DATA_PATH_TEST_ENV = _w2_fs1_knps_test_env / "Testumgebung" / "EasternGraphics" / "kn"
    EXPORT_DATA_PATH_DEFAULT = _w2_fs1_knps_test_env / "ofml_development" / "Tools" / "ofml_datenmacher"
    ROOT_PROJECT_FOLDER = _root_project_path
    CREATE_EBASE_EXE = (_root_project_path / "tools" / "windows" / "ebmkdb.exe"
                        if OS_NAME == "windows"
                        else Path("/app") / "tools" / "linux" / "ebmkdb"
                        )


assert Config.W2_FS1_KNPS_TEST_ENV is not None and Path(Config.W2_FS1_KNPS_TEST_ENV).exists()
assert Config.IMPORT_PLAINTEXT_PATH is not None and Path(Config.IMPORT_PLAINTEXT_PATH).exists()
print("Config.W2_FS1_KNPS_TEST_ENV", Config.W2_FS1_KNPS_TEST_ENV)
print("Config.IMPORT_PLAINTEXT_PATH", Config.IMPORT_PLAINTEXT_PATH)
print("Config.EXPORT_DATA_PATH_TEST_ENV", Config.EXPORT_DATA_PATH_TEST_ENV)
print("Config.EXPORT_DATA_PATH_DEFAULT", Config.EXPORT_DATA_PATH_DEFAULT)

