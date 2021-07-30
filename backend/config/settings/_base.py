import os

from django.core.exceptions import ImproperlyConfigured


def get_secret(setting: str) -> str:
    """Возрашает значения из окружения"""
    try:
        return os.getenv(setting)
    except KeyError:
        error_msg = f"Set the {setting} environment variable"
        raise ImproperlyConfigured(error_msg)

