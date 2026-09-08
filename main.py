import os
import sys
from pathlib import Path

# Ensure root directory is on sys.path
ROOT_DIR = Path(__file__).resolve().parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.server import app
from src.config import HOST, PORT

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.server:app", host=HOST, port=PORT, reload=True)
