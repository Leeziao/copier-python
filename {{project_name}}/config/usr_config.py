from pathlib import Path
import yaml
import os

from ..utils.singleton import Singleton
from .runtime_config import CONFIG_DIR

class Config(metaclass=Singleton):
    """
    常规使用方法：
    config = Config("config.yaml")
    secret_key = config.get_key("MY_SECRET_KEY")
    print("Secret key:", secret_key)
    """
    _instance = None
    default_yaml_file = Path(CONFIG_DIR) / 'config/config.yaml'

    def __init__(self, yaml_file=default_yaml_file):
        self._configs = {}
        self._init_with_config_files_and_env(self._configs, yaml_file)

    def _init_with_config_files_and_env(self, configs: dict, yaml_file):
        """从 config/config.yaml / env三处按优先级递减加载"""
        configs.update(os.environ)

        if not yaml_file.exists():
            return

        # Reading Local YAML File
        with open(yaml_file, 'r', encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)
            os.environ.update({k: v for k, v in yaml_data.items() if isinstance(v, str)})
            configs.update(yaml_data)

    def _get(self, *args, **kwargs):
        return self._configs.get(*args, **kwargs)

    def get(self, key, *args, **kwargs):
        """从config/key.yaml / config/config.yaml / env三处找值，找不到报错"""
        value = self._get(key, *args, **kwargs)
        if value is None:
            raise ValueError(f"Key '{key}' not found in environment variables or in the YAML file")
        return value


CONFIG = Config()

