import random
from typing import List
import pytest
from bosco.generate import generate_random_container


def test_generate_random_container_size():
    sizes = [0, 1, 5, 10]
    for size in sizes:
        container = generate_random_container(size)
        assert len(container) == size


def test_generate_random_container_elements_int():
    size = 10
    container = generate_random_container(size, type_="int")
    for element in container:
        assert isinstance(element, int)
        assert 1 <= element <= size * size


def test_generate_random_container_elements_float():
    size = 10
    container = generate_random_container(size, type_="float")
    for element in container:
        assert isinstance(element, float)
        assert 1 <= element <= size * size


def test_generate_random_container_elements_str():
    size = 10
    container = generate_random_container(size, type_="str")
    for element in container:
        assert isinstance(element, str)
        assert len(element) == 10


def test_generate_random_container_randomness():
    size = 5
    container1 = generate_random_container(size)
    container2 = generate_random_container(size)
    assert container1 != container2


def test_generate_random_container_return_type():
    size = 3
    container = generate_random_container(size)
    assert isinstance(container, list)


def test_generate_random_container_invalid_type():
    size = 5
    with pytest.raises(ValueError) as exc_info:
        generate_random_container(size, type_="invalid")
    assert str(exc_info.value) == "Unsupported type: invalid"
