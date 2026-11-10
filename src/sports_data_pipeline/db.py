"""Database connection helpers."""

import os

import psycopg
from dotenv import load_dotenv

def get_connection() -> psycopg.Connection:
    """Open a connection to the local PostgreSQL using settings from .env."""
    load_dotenv()
    return psycopg.connect(
        host="127.0.0.1",
        port=int(os.getenv("POSTGRES_PORT", "5432")),
        user=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASSWORD"],
        dbname=os.environ["POSTGRES_DB"],
    )
