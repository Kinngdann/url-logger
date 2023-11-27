from file_io import save_new_url
from .get_input_with_attempts import get_input_with_attempts

import sys
sys.path.append("..")


def add_new_url():
    query_keys = [
        "URL",
        "interval",
        "duration",
        "downtime_alert"
    ]

    query_input_hints = [
        "URL to query. *required",
        "Interval for querying Ex. (1s, 5m, 1h) *required",
        "Duration for querying Ex. (30m, 1h, 2d, 1mth) *required",
        "Send downtime alert? Ex. ('yes/no'). Default: No"
    ]

    query_info_staging = {key: get_input_with_attempts(key, query_keys[i]) for i, key in enumerate(query_input_hints)}
    query_info = {key: query_info_staging[query_input_hints[i]] for i, key in enumerate(query_keys)}

    save_new_url(query_info)
