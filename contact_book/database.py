# database.py
import duckdb

class Database:
    def __init__(self, db_path='contact_book.db'):
        self.db_path = db_path
        self.connection = None

    def connect(self):
        if self.connection is None:
            self.connection = duckdb.connect(self.db_path)
            self._initialize_database()

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    def _initialize_database(self):
        self.connection.execute('''
            CREATE SEQUENCE IF NOT EXISTS contact_id_seq START 1;
        ''')
        self.connection.execute('''
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER DEFAULT nextval('contact_id_seq'),
                name TEXT,
                phone TEXT,
                email TEXT
            )
        ''')
