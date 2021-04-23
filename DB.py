import sqlite3

def createdb():
    # Creating and connecting to the Database
    conn = sqlite3.connect('data.db')
    # Create a cursor
    c = conn.cursor()
    # Create a Table Datatype text
    c.execute("CREATE TABLE data (name text, username text, password text)")
    # Commit our command
    conn.commit()

def insertdb(name, username, password):
    # Creating and connecting to the Database
    conn = sqlite3.connect('data.db')
    # Create a cursor
    c = conn.cursor()
    # Inserting Data
    c.execute("INSERT INTO data (name, username, password) VALUES (?,?,?)",(name, username, password))
    # Commit our command
    conn.commit()

def fetchall():
    # Creating and connecting to the Database
    conn = sqlite3.connect('data.db')
    # Create a cursor
    c = conn.cursor()
    # Getting formated contents
    c.execute("SELECT rowid, * FROM data")

    info = c.fetchall()
    print("ID" +"\tUsername" +"\tPassword" +"\tName")
    print("--" +"\t--------" +"\t--------"+"\t----")
    for i in info:
        print (str(i[0]) +"\t\t" + i[1]+"\t\t" + i[2]+"\t\t" + i[3])

    # Commit our command
    conn.commit()

def delete(id):
    # Creating and connecting to the Database
    conn = sqlite3.connect('data.db')
    # Create a cursor
    c = conn.cursor()
    # Inserting Data
    c.execute("DELETE from data WHERE rowid = {}".format(id))
    # Commit our command
    conn.commit()

def closedb():
    # Close our connection
    conn.close()
