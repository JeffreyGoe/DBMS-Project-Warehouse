from items import *

class Inventory:
    def __init__(self) -> None:
        self.__items: dict = {}
    
    def getInv(self) -> dict:
        from copy import deepcopy
        return deepcopy(self.__items)

    def addItem(self, new_item: Item, stock: int) -> bool:
        new_name: str = new_item.get_Item_Name()
        for row in self.__items:
            item: Item = row
            if item.get_Item_Name == new_name:
                    return None
        self.__items[new_item] = stock
    
    def  getItem(self, name: str) -> 'list[Item]':
        items: list[Item] = []
        for row in self.__items:
            item: Item = row
            if item.get_Item_Name() == name:
                items.append(item)
        if len(items) == 0:
            return None
        
        return items

    

def getStock(self, name: str, category: str) -> int:
    for row in self.__items:
        item: Item = row
        if item.get_Item_Name() == name:
            return self.__items[item]
        return None

def load(self):
    from typing import Any
    from items import get_items

    items: list[Any] = get_items()
    Inventory: list[Any] = get_inventory()
    for row in Inventory:
        for row2 in items:
            if row[0] == row2[0]:
                item = Item(row2[0],row2[1],row2[2],row2[3])    
                stock: int = row[1]
                self.addItem(item, stock)

def load_db() -> None:
    import sqlite3 as sql
    from sqlite3.dbapi2 import Connection, _Cursor
    from typing import Any
    from items import get_items
        
    try: 
        connect: Connection = sql.connect('warehouse.db')
        cur: _Cursor = connect.cursor()
        items: list[Any] = get_items()
        stock: int = 1

        for item in items:
            cur.execute("INSERT INTO Inventory (Item_Name, stock) VALUES (?,?)", (item[0], stock))
            stock: int = stock * 5
    except sql.IntegrityError:

        cur.commit()
        cur.close()

def insert_item(name: str, price: float) -> None:
    import sqlite3 as sql
    from sqlite3.dbapi2 import Connection, Cursor

    connect: Connection = sql.connect('warehouse.db')
    cur: Cursor = connect.cursor()

    try:
        cur.execute("INSERT INTO Warehouse (Item_Name, item_price) VALUES (?,?)", (name, price))
    except sql.IntegrityError:
        print("Item already exists")
    connect.commit()
    connect.close()
      
def get_inventory() -> list:
    import sqlite3 as sql
    from sqlite3.dbapi2 import Connection, _Cursor
    from typing import Any

    connect: Connection = sql.connect('warehouse.db')
    cur: _Cursor = connect.cursor()
    cur.execute("SELECT * FROM Inventory")
    rows: list[Any] = cur.fetchall()
    connect.commit()
    connect.close()
    return rows


    
