import sqlite3
from config import DB_PATH

def get_connection():
    """Returns a fresh SQLite connection."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # lets us access columns by name like a dict
    return conn