from typing import Any

class Item:
    def __init__(self,Item_Id:int, Item_Name: str, item_quantity: int) -> None:
        self.__Item_Id: int = Item_Id
        self.__Item_Name: str = Item_Name
        self.__item_quantity: int = item_quantity

    def get_item_id(self) -> int:
        return self.__Item_Id

    def get_Item_Name(self) -> str:
        return self.__Item_Name

    def get_item_quantity(self) -> int:
        return self.__item_quantity
        
class Cart:
    def __init__(self, username: str) -> None:
        self.__username: str = username
        self.__cart: dict = {}
        
def search_item(Item_Name: str) -> 'list':
    import sqlite3
    connect = sqlite3.connect('warehouse.db')
    cur = connect.cursor()
    cur.execute("SELECT * FROM Warehouse WHERE Item_Name = ?", (Item_Name,))
    Row:list[Any] = cur.fetchall()
    connect.commit()
    connect.close()
    return Row
        
def insert_item(Item_Name: str, item_quantity: int, item_price: int) -> None:
    import sqlite3
    import sqlite3.dbapi2
    connect = sqlite3.connect('warehouse.db')
    cur = connect.cursor()
    try:
        Rows: list[Any] = search_item(Item_Name)

        if Rows is not None:
            cur.commit()
            cur.close()
            return None

        query = "INSERT INTO Warehouse (Item_Name, item_quantity, item_price) VALUES (Item_Name, item_quantity)"
        cur.execute(query, {'Item_Name': Item_Name, 'item_quantity': item_quantity})
    except sqlite3.dbapi2.IntegrityError:
        print("Item already exists")
    cur.commit()
    cur.close()

def remove_item(Item_Name: str) -> None:
    import sqlite3
    connect = sqlite3.connect('warehouse.db')
    cur = connect.cursor()
    cur.execute("DELETE FROM Warehouse WHERE Item_Name = ?", (Item_Name,))
    connect.commit()
    connect.close()

def get_items() -> list:
    import sqlite3
    connect = sqlite3.connect('warehouse.db')
    cur = connect.cursor()
    cur.execute("SELECT * FROM Warehouse")
    Rows: list[Any] = cur.fetchall()
    connect.commit()
    connect.close()
    return Rows

def get_cart(Username: str) -> list:
    import sqlite3
    connect = sqlite3.connect('warehouse.db')
    cur = connect.cursor()
    cur.execute("SELECT * FROM Cart Where username = ?", (Username,))  
    Rows: list[Any] = cur.fetchall()
    connect.commit()
    connect.close()
    return Rows
    
def add_item_to_cart(Username: str, Item_Id: int, Item_Quantity: int) -> None:
    import sqlite3
    import sqlite3.dbapi2
    connect = sqlite3.connect('warehouse.db')
    cur = connect.cursor()
    try:
        query = "INSERT INTO Cart (Username, Item_Id, Item_Quantity) VALUES (Username, Item_Id, Item_Quantity)"
        cur.execute(query, {'Username': Username, 'Item_Id': Item_Id, 'Item_Quantity': Item_Quantity})
    except sqlite3.dbapi2.IntegrityError:
        print("Item already exists")
    cur.commit()
    cur.close()

def Update_item_in_cart(Username: str, Item_Name: str, Item_Quantity: int) -> None:
    import sqlite3
    import sqlite3.dbapi2
    connect = sqlite3.connect('warehouse.db')
    cur = connect.cursor()
    try:
        query = "UPDATE Cart SET Item_Quantity = ? WHERE Username = ? AND Item_Name = ?"
        cur.execute(query, {'Username': Username, 'Item_Name': Item_Name, 'Item_Quantity': Item_Quantity})
    except sqlite3.dbapi2.IntegrityError:
        print("Item doesn't exist")
    cur.commit()
    cur.close()
def remove_item_from_cart(Username: str, Item_Name: str,Item_Quantity) -> None:
    import sqlite3
    import sqlite3.dbapi2
    connect = sqlite3.connect('warehouse.db')
    cur = connect.cursor()
    try:
        query = "DELETE FROM Cart WHERE Username = ? AND Item_Name = ? AND Item_Quantity = ?"
        cur.execute(query, {'Username': Username, 'Item_Name': Item_Name, 'Item_Quantity': Item_Quantity})
    except sqlite3.dbapi2.IntegrityError:
        print("Item doesn't exist")
    cur.commit()
    cur.close()





 