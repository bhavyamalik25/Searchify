import os

# SQLite database file path — stored in the project folder
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "searchify.db")