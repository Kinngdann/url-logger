import re
from typing import Union


def name_validator(name: str) -> Union[str, bool]:
    if name is None:
        name = "Anonymous"

    if match := re.search(r"^([\w\- ']+)$", name.strip().lower(), re.IGNORECASE):
        return match.group(1)

    return False
