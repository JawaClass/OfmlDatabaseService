import copy
import sys
from loguru import logger

logger.remove()
_EMPTY_TEMPLATE_LOGGER = copy.deepcopy(logger)
logger.add(sys.stderr)


def new_loguru_logger():
    return copy.deepcopy(_EMPTY_TEMPLATE_LOGGER)
