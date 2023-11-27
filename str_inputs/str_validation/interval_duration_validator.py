from typing import Union
import re


def interval_validator(period: str) -> Union[str, bool]:
    if period is None:
        return False
    accepted_interval_units = ["s", "m", "h", "d"]

    if match := re.search(r"^(\d+)(s|m|h|d|)$", period, re.IGNORECASE):
        if match.group(2) in accepted_interval_units:
            return f"{match.group(1)}{match.group(2)}"

    return False


def duration_validator(period: str) -> Union[str, bool]:
    if period is None:
        return False
    accepted_duration_units = ["m", "h", "d", "mth"]

    if match := re.search(r"^(\d+)(m|h|d|mth)$", period, re.IGNORECASE):
        if match.group(2) in accepted_duration_units:
            return f"{match.group(1)}{match.group(2)}"

    return False
