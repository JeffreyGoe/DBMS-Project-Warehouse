#GUI for DB project
import os
import sqlite3
from Customer import Customer
from Cart import Cart




def clear_screen():
    os.system('cls')

def view_item():
    clear_screen()

    #connect to DB and create cursor
    sqliteCon = sqlite3.connect('warehouse.db')
    cursor = sqliteCon.cursor()

    #sql command definition and execution
    sql_command = """SELECT * item"""
    cursor.execute(sql_command)

    print("select one of the following")
    print("1. add item")
    print("2. back")

    #disconnect from DB
    sqliteCon.close()

def view_cart():
    clear_screen()
    Customer.get_username()
    cart_copy, total = Cart.get_cart()
    for row in cart_copy:
        item: Item = row
        print(f"{item}")



    print("select one of the following")
    print("1. delete item")
    print("2. checkout")
    print("3. back")

def add_item():
    clear_screen()
    item_num = input("enter the item number: ")
    quantity = input("how many do you want: ")
    #INSERT INTO cust_cart(username, item_num, quantity)

def delete_item():
    clear_screen()
    current_item_num = input("enter item num you want to delete from cart: ")
    #DELETE FROM cust_cart WHERE item_num IS current_item_num, username IS current_user

def checkout():
    #UPDATE warehouse SET quantity = quantity - user_quantity WHERE item_num IS userCart_item_num
        #continue to update until all cart items for user are taken care of then delete
    #DELETE FROM cust_cart WHERE username IS current_user
    print("thank you for your purchase")

def gui():
    clear_screen()
    print("select one of the following")
    print("1. view items")
    print("2. view cart")
    print("3. logout")
    choice = input("enter you choice: ")
    #VIEW ITEM
    if choice == '1':
        view_item()
        choice = input("enter you choice: ")
        #ADD ITEM
        if choice == '1':
            add_item()
            gui()
        #BACK
        elif choice == '2':
            gui()
        else:
            clear_screen()
            print("not a valid option. try again.")
            gui()
    #VIEW CART
    elif choice == '2':
        view_cart()
        choice = input("enter you choice: ")
        #DELETE
        if choice == '1':
            delete_item()
            gui()
        #CHECKOUT
        elif choice == '2':
            checkout()
            gui()
        #BACK
        elif choice == '3':
            gui()
        else:
            print("not a valid option. try again.")
            gui()
    #LOGOUT
    elif choice == '3':
        main()
    else:
        print("not a valid option. try again.")
        gui()

def main():
    logged_in: bool = False
    run: bool = True
    logged_in = False
    clear_screen()
    print("select one of the following")
    print("1. login")
    print("2. exit")
    choice = input("enter your choice: ")

    if choice == '1':
        clear_screen()
        user = input("username: ")
        password = input("password: ")
        #check db for match
        if user == password:
            gui()

    elif choice == '2':
        exit()
    else:
        print("not a valid option. try again.")
        main()


main()
