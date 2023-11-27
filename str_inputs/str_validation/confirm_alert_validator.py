import re
from typing import Union


def confirm_alert_validator(alert: str = True) -> Union[bool, None]:
    if alert is None:
        return False

    if match := re.search(r"^(\w+)$", alert.lower(), re.IGNORECASE):
        confirm = match.group(1)
        return True if confirm in ["yes", "y"] else (False if confirm in ["no", "n"] else None)

    return False
