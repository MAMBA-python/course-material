"""
Database already created:

CREATE TABLE contacts (
	id SERIAL NOT NULL,
	name VARCHAR(50) NOT NULL,
	email VARCHAR(50) NOT NULL,
CONSTRAINT contacts_pkey PRIMARY KEY (id));
"""


import os
import psycopg2

def connect(db, user, password, host="localhost", port=5432):
    """
    Connects to the database and ensures there are tables.
    """
    conn = psycopg2.connect(**{
        "database": db,
        "user": user,
        "password": password,
        "host": host,
        "port": port

    })
    return conn

def insert(name, email, conn=None):
    if not conn: conn = connect()
    
    cursor = conn.cursor()
    sql = "INSERT INTO contacts (name, email) VALUES  (%s, %s)"
    cursor.execute(sql, (name, email))
    conn.commit()

if __name__ == "__main__":
    name  = raw_input("Enter name: ")
    email = raw_input("Enter email: ")
    conn  = connect("contacts", "example", "password")
    insert(name, email, conn)

    cursor = conn.cursor()
    cursor.execute("SELECT count(id) FROM contacts")
    contacts = cursor.fetchone()[0]
    print "There are now %i contacts" % contacts

    conn.close()
