"""Instalador de dependencias del proyecto.

Uso:
    python requirements.py
"""

import subprocess
import sys

DEPENDENCIES = [
    "fastapi",
    "uvicorn",
    "sqlalchemy",
    "python-dotenv",
    "psycopg2-binary",
    "pytest",
    "httpx",
]


def install_dependencies() -> None:
    for package in DEPENDENCIES:
        print(f"Instalando {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])


if __name__ == "__main__":
    install_dependencies()
