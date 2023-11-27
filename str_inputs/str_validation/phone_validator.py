import re
from typing import Union


def phone_validator(phone: str) -> Union[str, bool]:
    if phone is None:
        phone = "+2348036576333"

    if match := re.search(r"^(\+\d{13})$", phone):
        return match.group(1)

    return False
