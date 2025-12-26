from pathlib import Path
import os
from dotenv import load_dotenv

# Load .env from project root (falls back to current environment if not present)
project_root = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=project_root / ".env")

def _get_required(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Environment variable `{name}` is required. Add it to the environment or to {project_root / '.env'}.")
    return value

NASDAQ_FILE_PATH = _get_required("NASDAQ_FILE_PATH")
DAX_FILE_PATH = _get_required("DAX_FILE_PATH")
