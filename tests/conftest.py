from custom_python_logger import build_logger

logger = build_logger(project_name=LOGGER_NAME, log_file=True)
logger.debug("Starting pytest-collect-requirements tests")
