import pytest
from custom_python_logger import get_logger

from pytest_collect_requirements import LOGGER_NAME

logger = get_logger(LOGGER_NAME)


@pytest.mark.integration
@pytest.mark.requirements(cloud_instance="c5.large", region="eu-west-1")
def test_requirements() -> None:
    assert 1 == 1  # pylint: disable=R0133,R0124


@pytest.mark.integration2
@pytest.mark.requirements(cloud_instance="c5.small", region="eu-west-2")
def test_requirements2() -> None:
    assert 1 == 1  # pylint: disable=R0133,R0124
