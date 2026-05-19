from custom_python_logger import get_logger
from dotenv import load_dotenv

from pytest_collect_requirements.consts import LOGGER_NAME

load_dotenv()

logger = get_logger(LOGGER_NAME)
