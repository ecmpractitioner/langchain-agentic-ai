import os
from dotenv import load_dotenv


def load_and_return_api_key(api_key_name: str) -> str | None:
    """Load an environment variable from the local .env file."""
    if not api_key_name:
        return None

    load_dotenv(override=True)
    return os.getenv(api_key_name)
