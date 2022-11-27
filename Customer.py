from db import *
import sqlite3
class Customer:
    def __init__(self, username, password, birthday, address, phone_number, email):
        self.username = username
        self.password = password
        self.birthday = ""
        self.address = ""
        self.phone_number = ""
        self.email = ""

    def setUsername(self, username):
        connect = sqlite3.connect('warehouse.db')
        cur = connect.cursor()
        cur.execute("UPDATE Customer SET username = ? WHERE username = ?", (username, self.username))
        cur.execute("update Cart set username = ? where username = ?", (username, self.username))
        cur.execute("update Order set username = ? where username = ?", (username, self.username))
        connect.commit()
        connect.close()
        self.__username = username

    def setPassword(self, password):
        connect = sqlite3.connect('warehouse.db')
        cur = connect.cursor()
        cur.execute("UPDATE Customer SET password = ? WHERE username = ?", (password, self.username))
        connect.commit()
        connect.close()

        self.__password = password

        
    def setBirthday(self, birthday):
        connect = sqlite3.connect('warehouse.db')
        cur = connect.cursor()
        cur.execute("UPDATE Customer SET birthday = ? WHERE username = ?", (birthday, self.username))
        connect.commit()
        connect.close()
        self.__birthday = birthday

    def setAddress(self, address):
        connect = sqlite3.connect('warehouse.db')
        cur = connect.cursor()
        cur.execute("UPDATE Customer SET address = ? WHERE username = ?", (address, self.username))
        connect.commit()
        connect.close()
        self.__address = address

    def login(self):
        from items import insert_item
        from items import create_table

        connect = sqlite3.connect('warehouse.db')
        cur = connect.cursor()

        CreateTables()
        cur.execute("SELECT * FROM Customer WHERE username = ? AND password = ?", (self.username, self.password))
        row = cur.fetchone()

        if row is None:
            validated = False
        else:
        
            if len(row) > 2:
                if row[2] is not None:
                    self.__address = row[2]
                if row[3] is not None:
                    self.__birthday = row[3]
                if row[4] is not None:
                    self.__phone_number = row[4]
                if row[5] is not None:
                    self.__email = row[5]
        return validated



    def create_account(self):

        connect = sqlite3.connect('warehouse.db')
        cur = connect.cursor()

        CreateTables()
        cur.exectute('Select * from Customer where username = ?', (self.username,))
        row = cur.fetchall()
        if len(row) == 0:
            not_taken = True
        else: 
            not_taken = False
        
        if not_taken is True:
            cur.execute("Insert into Customer VALUES (?, ?, ?, ?, ?, ?)", (self.username, self.password, self.birthday, self.address, self.phone_number, self.email))
            connect.commit()
            result = True
        else: 
            result = False
        connect.close()
        return result

    def delete_account(self):
        connect = sqlite3.connect('warehouse.db')
        cur = connect.cursor()
        cur.execute("DELETE FROM Customer WHERE username = ?", (self.username,))
        connect.commit()
        connect.close()
        return


    def getOrderHistory(self):
        connect = sqlite3.connect('warehouse.db')
        cur = connect.cursor()
        cur.execute("SELECT * FROM Order WHERE username = ?", (self.username,))
        orders = cur.fetchall
        return orders
