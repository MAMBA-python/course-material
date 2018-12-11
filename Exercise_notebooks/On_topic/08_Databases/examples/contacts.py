import os
import sqlite3

def create_tables(conn):
    conn.execute("CREATE TABLE contacts (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT)")
    conn.commit()

def connect(path="contacts.db", syncdb=False):
    """
    Connects to the database and ensures there are tables.
    """
    if not os.path.exists(path):
        syncdb=True

    conn = sqlite3.connect(path)
    if syncdb:
        create_tables(conn)
    
    return conn

def insert(name, email, conn=None):
    if not conn: conn = connect()

    sql = "INSERT INTO contacts (name, email) VALUES  (?, ?)"
    conn.execute(sql, (name, email))
    conn.commit()

if __name__ == "__main__":
    name  = raw_input("Enter name: ")
    email = raw_input("Enter email: ")
    conn  = connect()
    insert(name, email, conn)

    contacts = conn.execute("SELECT count(id) FROM contacts").fetchone()[0]
    print "There are now %i contacts" % contacts

    conn.close()
