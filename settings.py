import os
from pathlib import Path
from dotenv import load_dotenv


def get_os_type_name():
    import platform
    system = platform.system()
    if system.lower() == "windows":
        return "windows"
    return "linux"


def _resolve_env(name: str):
    value = os.environ.get(name, None)
    assert value is not None, f"ENV missing: {name}"
    return value


def _ensure_path_exists(path: Path):
    assert path.exists(), f"Path '{path}' doesn't exist."

""" project root absolute path """
_root_project_path = Path(os.path.dirname(os.path.abspath(__file__)))

""" assert connection to w2_fs1 drive """
_w2_fs1_knps_test_env = _resolve_env("W2_FS1_DRIVE_KNPS_TESTUMGEBUNG")
_w2_fs1_knps_test_env = Path(_w2_fs1_knps_test_env)
_ensure_path_exists(_w2_fs1_knps_test_env)

""" load environment variables """
load_dotenv(_root_project_path / ".env")


class Config:
    OS_NAME = get_os_type_name()
    W2_FS1_KNPS_TEST_ENV = _w2_fs1_knps_test_env
    SECRET_KEY = "dev"
    MYSQL_USER = _resolve_env("MYSQL_USER")
    MYSQL_PASSWORD = _resolve_env("MYSQL_PASSWORD")
    MYSQL_SERVER = _resolve_env("MYSQL_SERVER")
    MYSQL_DATABASE = _resolve_env("MYSQL_DATABASE")
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_SERVER}/{MYSQL_DATABASE}"
    IMPORT_PLAINTEXT_PATH = _w2_fs1_knps_test_env / "ofml_development" / "repository" / "kn"
    EXPORT_DATA_PATH_TEST_ENV = _w2_fs1_knps_test_env / "Testumgebung" / "EasternGraphics" / "kn"
    EXPORT_DATA_PATH_DEFAULT = _w2_fs1_knps_test_env / "ofml_development" / "Tools" / "ofml_datenmacher"
    ROOT_PROJECT_FOLDER = _root_project_path
    CREATE_EBASE_EXE = (_root_project_path / "tools" / "windows" / "ebmkdb.exe"
                        if OS_NAME == "windows"
                        else _root_project_path / "tools" / "linux" / "ebmkdb"
                        )

""" make sure path we depend on exists """
_ensure_path_exists(Config.IMPORT_PLAINTEXT_PATH)
_ensure_path_exists(Config.CREATE_EBASE_EXE)


