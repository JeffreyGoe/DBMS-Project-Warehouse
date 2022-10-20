#Create the tables


def create_customer_table():
    import sqlite3
    connect = sqlite3.connect('warehouse.db')
    cur = connect.cursor()
    #creates database query
    cur.execute("""CREATE TABLE IF NOT EXISTS Customer (
                username TEXT UNIQUE PRIMARY KEY,
                password TEXT,
                birthday TEXT);
                """)
    #commit and close the connection
    connect.commit()
    connect.close()


def create_items_table():
    import sqlite3
    connect = sqlite3.connect('warehouse.db')
    cur = connect.cursor()
    #creates database query
    cur.execute("""CREATE TABLE IF NOT EXISTS ITEMS (
                username TEXT UNIQUE PRIMARY KEY,
                password TEXT,
                birthday TEXT);
                """)
    #commit and close the connection
    connect.commit()
    connect.close()

def create_table(query):
    import sqlite3
    connect = sqlite3.connect('warehouse.db')
    cur = connect.cursor()
    #creates database query
    try:
        cur.execute(query)
    except sqlite3.OperationalError:
        ...

    #commit and close the connection
    connect.commit()
    connect.close()
