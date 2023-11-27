import re
from typing import Union


def email_validator(email: str) -> Union[str, bool]:
    if email is None:
        return ""

    if match := re.search(r"^([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$", email.strip().lower(), re.IGNORECASE):
        return match.group(1)

    return False
