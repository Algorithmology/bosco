"""Generate random container."""

import random
from typing import List


def generate_random_container(
    size: int,
) -> List[int]:
    """Generate a random list defined by the size."""
    random_list = [random.randint(1, size * size) for _ in range(size)]
    return random_list