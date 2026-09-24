import os

from dotenv import load_dotenv


# Load variables from .env
load_dotenv()


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()

GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-3.8-flash"
).strip()

BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "http://127.0.0.1:8000"
).strip()


def validate_config():
    """
    Check whether the required Gemini API key exists.
    """
    if not GEMINI_API_KEY:
        raise ValueError(
            "GEMINI_API_KEY is missing. "
            "Please add your Gemini API key to the .env file."
        )