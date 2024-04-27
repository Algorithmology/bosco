import random
import string
from typing import List, Union


def generate_random_container(
    size: int,
    type_: str = "int",
) -> List[Union[int, float, str]]:
    """Generate a random list defined by the size and element type."""
    if type_ == "int":
        random_list = [random.randint(1, size * size) for _ in range(size)]
    elif type_ == "float":
        random_list = [random.uniform(1, size * size) for _ in range(size)]
    elif type_ == "str":
        random_list = [
            "".join(random.choices(string.ascii_letters + string.digits, k=10))
            for _ in range(size)
        ]
    else:
        raise ValueError(f"Unsupported type: {type_}")

    return random_list
