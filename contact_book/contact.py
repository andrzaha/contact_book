# contact.py
from database import Database

class Contact:
    def __init__(self):
        self.db = Database()
        self.db.connect()

    def add_contact(self, name, phone, email):
        self.db.connection.execute('''
            INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)
        ''', (name, phone, email))

    def remove_contact(self, contact_id):
        self.db.connection.execute('''
            DELETE FROM contacts WHERE id = ?
        ''', (contact_id,))

    def get_contacts(self):
        result = self.db.connection.execute('SELECT * FROM contacts').fetchall()
        return result

    def __del__(self):
        self.db.close()
