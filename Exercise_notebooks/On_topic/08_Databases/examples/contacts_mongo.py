from pymongo import MongoClient
from datetime import datetime

def connect(database="contacts", host="localhost", port=27017):
    """
    Connects to the database 
    """
    client = MongoClient(host, port)
    return client[database]

if __name__ == "__main__":
    entry = {
        "name": raw_input("Enter name: "),
        "email": raw_input("Enter email: "),
        "created": datetime.now()
    }

    while True:
        key = raw_input("Add key: ")
        if not key: break
        val = raw_input("Add val: ")
        if not val: break
        entry[key] = val

    db = connect()
    collection = db.contacts

    collection.insert(entry)
    print "There are now %i documents in contacts" % collection.count()
