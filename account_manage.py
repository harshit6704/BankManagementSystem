# account_management.py
import mysql.connector
import database

def create_account():
    conn = database.connect()
    c = conn.cursor()
    
    try:
        ac_n = int(input("Enter Account Number : "))
        n = input("Enter Name : ")
        p = input("Enter Password : ")
        ac_balance = int(input("Enter Amount : "))
        ac_t = input("Enter Account Type (C/S): ")
        
        s = "INSERT INTO bank(ac_n, name, password, ac_balance, ac_t) VALUES (%s, %s, %s, %s, %s)"
        values = (ac_n, n, p, ac_balance, ac_t)
        
        c.execute(s, values)
        conn.commit()
        print("Record Inserted")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        database.close_connection(conn)

def show_records():
    conn = database.connect()
    c = conn.cursor()
    
    try:
        qry = "SELECT * FROM bank"
        c.execute(qry)
        
        for data in c.fetchall():
            print("Acc_No ", "Name", "Password", "Balance" ,"Type\n",data[0], data[1],data[2],data[3],data[4])
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        database.close_connection(conn)

def Balance_Enc():
    conn = database.connect()
    c = conn.cursor()
    
    try:
        ac_n = int(input("Enter Account Number : "))
        s= "SELECT * FROM bank WHERE ac_n='%d'"%(ac_n)
        c.execute(s)
        for data in c.fetchall():
            print("Acc_No ", "Name", "Password", "Balance" ,"Type\n",data[0], data[1],data[2],data[3],data[4])
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        database.close_connection(conn)

# Adjust other functions similarly

def dep_Amount():
    conn = database.connect()
    c = conn.cursor()
    
    try:
        ac_n= int(input("Enter Account Number : "))
        amount = int(input("Enter Amount : "))
        
        s = "SELECT ac_balance FROM bank WHERE ac_n='%d'"%(ac_n)
        c.execute(s)
        
        for data in c.fetchall():
            ac = data[0]
        
        total_amount = ac + amount
        s1 = "UPDATE bank SET ac_balance='%d' WHERE ac_n='%d'"%(total_amount,ac_n)
        r = c.execute(s1)
        
        if r != 0:
            print("Record Updated : ", total_amount)
        else:
            print("Record Not Updated")
        
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        database.close_connection(conn)

# Similarly adjust other functions like Withdraw_Amount(), clos_ac(), mod_acc()
