import random
import string
from typing import List, Union


def generate_random_container(
    size: int,
    type_: str = "int",
) -> List[Union[int, float, str]]:
    """Generate a random list defined by the size and element type."""
    if type_ == "int":
        # Generate a list of random integers within the range [1, size*size]
        random_list = [random.randint(1, size * size) for _ in range(size)]
    elif type_ == "float":
        # Generate a list of random floating-point numbers within the range [1, size*size]
        random_list = [random.uniform(1, size * size) for _ in range(size)]
    elif type_ == "str":
        # Generate a list of random strings of length 10 composed of letters and digits
        random_list = [
            "".join(random.choices(string.ascii_letters + string.digits, k=10))
            for _ in range(size)
        ]
    else:
        # Raise an error if an unsupported type is specified
        raise ValueError(f"Unsupported type: {type_}")

    return random_list  # Return the generated random list
