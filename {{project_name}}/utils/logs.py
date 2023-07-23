import sys
from pathlib import Path
from datetime import datetime
from loguru import logger as _logger

from ..config import *


def define_log_level(print_level="INFO", logfile_level="DEBUG"):
    _logger.remove()
    _logger.add(sys.stderr, level=print_level)
    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + '.txt'
    _logger.add(Path(LOG_DIR) / filename, level=logfile_level)
    return _logger


logger = define_log_level()

