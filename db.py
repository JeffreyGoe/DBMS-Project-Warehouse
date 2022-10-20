#Create the tables

# if any of these don't work change all to capital letters.
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




def create_warehouse_table():
    query = """CREATE TABLE IF NOT EXISTS Warehouse (
        ItemID INTEGER PRIMARY KEY, AutoIncrement,
        Item_Name TEXT NOT NULL,
        Item_Quantity INTEGER NOT NULL,
        Item_Price INTEGER NOT NULL,

        """
    create_table(query)

    #Creating another table for items seems redudant so I will not be adding one unless necessary

def create_cart_table():
    query = """CREATE TABLE IF NOT EXISTS Cart (
        CartID INTEGER PRIMARY KEY, AutoIncrement,
        username text NOT NULL,
        Item_id INTEGER NOT NULL,
        Item_Quantity INTEGER NOT NULL,
        Item_Price INTEGER NOT NULL,
        'Foreign Key' (username) REFERENCES Customer(username)
        'Foreign Key' (Item_id) REFERENCES Warehouse(Item_id)
        """
    create_table(query)
def create_order_table():
    query = """CREATE TABLE IF NOT EXISTS Order (
        OrderID INTEGER PRIMARY KEY, AutoIncrement,
        username text NOT NULL,
        Item_id INTEGER NOT NULL,
        Item_Quantity INTEGER NOT NULL,
        'Foreign Key' (username) REFERENCES Customer(username)
        'Foreign Key' (Item_id) REFERENCES Warehouse(Item_id)
        """
    create_table(query)


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