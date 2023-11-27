# from .str_validation import url_validator
from .str_validation import map_validator


def get_input_with_attempts(hint: str, validator_type: str) -> str:
    str_input_attempt = 3

    while str_input_attempt != 0:
        data = input(f"{hint}: ")

        if data == "":
            data = None

        validator = map_validator(validator_type)
        valid = validator(data)

        if valid or valid == "":
            return valid

        if validator_type == "downtime_alert" and valid is not None:
            return valid

        str_input_attempt -= 1

    raise ValueError(f"Invalid {validator_type}, process is cancelled")
