from .url_validator import url_validator
from .interval_duration_validator import duration_validator, interval_validator
from .confirm_alert_validator import confirm_alert_validator
from .name_validator import name_validator
from .phone_validator import phone_validator
from .email_validator import email_validator


def map_validator(validator_type: str):
    validator = {
        "name": name_validator,
        "phone": phone_validator,
        "email": email_validator,
        "URL": url_validator,
        "interval": interval_validator,
        "duration": duration_validator,
        "downtime_alert": confirm_alert_validator
    }

    if validator_type in validator:
        return validator[validator_type]

    raise Exception("Validation type not specified")
