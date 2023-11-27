from .get_input_with_attempts import get_input_with_attempts
from file_io import save_new_user


def add_user():
    user_keys = ["name", "phone", "email"]
    user_input_hints = [
        "What's your name? (optional)",
        "Enter your phone number *required",
        "Enter your email (optional)"
    ]

    user_info = {key: get_input_with_attempts(user_input_hints[i], key) for i, key in enumerate(user_keys)}
    save_new_user(user_info)


