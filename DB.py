import sqlite3

def createdb():
    # Creating and connecting to the Database
    conn = sqlite3.connect('data.db')
    # Create a cursor
    c = conn.cursor()
    # Create a Table Datatype text
    c.execute("CREATE TABLE data (username text, password text)")
    # Commit our command
    conn.commit()

def insertdb(username, password):
    # Creating and connecting to the Database
    conn = sqlite3.connect('data.db')
    # Create a cursor
    c = conn.cursor()
    # Inserting Data
    c.execute("INSERT INTO data (username, password) VALUES (?,?)",(username, password))
    # Commit our command
    conn.commit()

def closedb():
    # Close our connection
    conn.close()
