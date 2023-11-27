import re
from typing import Union


def url_validator(url: str) -> Union[str, bool]:
    if url is None:
        return False

    if match := re.search(r"^(?:https?:\/\/)?(?:www\.)?(\w+\.(com|net|org|edu))$", url.lower(), re.IGNORECASE):
        return match.group(1)

    return False
