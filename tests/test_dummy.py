from typing import Any

import pytest
from custom_python_logger import get_logger

logger = get_logger(__name__)


def requirements(**kwargs: Any) -> Any:
    return pytest.mark.requirements(**kwargs)


@pytest.mark.integration
@requirements(cloud_instance="c5.large", region="eu-west-1")
def test_requirements() -> None:
    print()
    assert 1 == 1  # pylint: disable=R0133,R0124


@requirements(cloud_instance="c5.small", region="eu-west-2")
def test_requirements2() -> None:
    print()
    assert 1 == 1  # pylint: disable=R0133,R0124
