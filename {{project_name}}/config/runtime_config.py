import os

RUNTIME_DIR = os.getcwd()

CONFIG_DIR = os.path.dirname(os.path.abspath(__file__))

APP_DIR = os.path.dirname(CONFIG_DIR)

ROOT_DIR = os.path.dirname(APP_DIR)

DATA_DIR = os.path.join(ROOT_DIR, "data")

LOG_DIR = os.path.join(ROOT_DIR, "logs")

dir_list = [DATA_DIR, LOG_DIR]
for dirname in dir_list:
    if not os.path.exists(dirname):
        os.makedirs(dirname)

