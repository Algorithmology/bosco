"""Confirm the correctness of the constants module."""

from dataclasses import FrozenInstanceError

import pytest

from bosco.constants import Bosco


@pytest.fixture
def bosco():
    """Return a Bosco instance for use in the tests."""
    return Bosco(
        Application_Name="bosco",
        Application_Author="BoscoTeam",
        Emoji=":dizzy:",
        Name="bosco",
        Programming_Language="python",
        Separator="/",
        Tagline="bosco: Measure the performance of Python functions!",
        Theme_Background="default",
        Theme_Colors="ansi_dark",
        Website=":link: GitHub: https://github.com/gkapfham/chasten",
    )


def test_number_of_constants(bosco):
    """Confirm that there are the correct number of constants."""
    assert len(bosco.__annotations__) == 10  # noqa: PLR2004


def test_default_values(bosco):
    assert bosco.Application_Name == "bosco"
    assert bosco.Application_Author == "BoscoTeam"
    assert bosco.Emoji == ":dizzy:"
    assert bosco.Name == "bosco"
    assert bosco.Programming_Language == "python"
    assert bosco.Separator == "/"
    assert (
        bosco.Tagline == "bosco: Measure the performance of Python functions!"
    )
    assert bosco.Theme_Background == "default"
    assert bosco.Theme_Colors == "ansi_dark"
    assert (
        bosco.Website == ":link: GitHub: https://github.com/gkapfham/chasten"
    )


def test_reassignment(bosco):
    with pytest.raises(FrozenInstanceError):
        bosco.Application_Name = "new_name"
