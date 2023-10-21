import sqlite3

DB_NAME = "clientes.db"


class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.commit()
        self.conn.close()

    def create_client_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            identificacion TEXT PRIMARY KEY,
            nombre TEXT,
            saldo REAL
        )
        ''')

    def add_client(self, identificacion, nombre, saldo=0):
        self.cursor.execute('INSERT INTO clientes (clientes.identificacion, nombre, saldo) VALUES (?, ?, ?)',
                            (identificacion, nombre, saldo))

    def get_client_by_identification(self, identificacion):
        self.cursor.execute("SELECT * FROM clientes WHERE clientes.identificacion = ?", (identificacion,))
        return self.cursor.fetchone()

    def update_client(self, identificacion, nombre, saldo):
        self.cursor.execute("UPDATE clientes SET nombre = ?, clientes.saldo = ? WHERE identificacion = ?",
                            (nombre, saldo, identificacion))

    def delete_client(self, identificacion):
        self.cursor.execute("DELETE FROM clientes WHERE clientes.identificacion = ?", (identificacion,))
