import mysql.connector
#import pymysql as sql
con = mysql.connector.connect(host='localhost',user='root',password='9654558088',database='banky')
c = con.cursor()

# Ceate new account
def Create_Account():
    ac_n = int(input("Enter Account Number : "))
    n = input("Enter Name : ")
    p = input("Enter Password : ")
    ac_balance = int(input("Enter Amount : "))
    ac_t = input("Enter Account Type (C/S): ")
    s = "insert into bank(ac_n,name,password,ac_balance,ac_t) values('%d','%s','%s','%d','%s')"%(ac_n,n,p,ac_balance,ac_t)
    r = c.execute(s)
    if(r!=0):
        print("Record Inserted  ")
    con.commit()
    
# Show all accounts
def show_Record():
    qry = "select * from bank"
    c.execute(qry)
    for data in c.fetchall():
        print("Acc_No ", "Name", "Password", "Balance" ,"Type\n",data[0], data[1],data[2],data[3],data[4])
    con.commit()

#Balance Enquiry
def Balance_Enc():
    ac_n = int(input("Enter Account Number : "))
    s= "select *from bank where ac_n='%d'"%(ac_n)
    c.execute(s)
    for data in c.fetchall():
        print("Acc_No ", "Name", "Password", "Balance" ,"Type\n",data[0], data[1],data[2],data[3],data[4])
    con.commit()

# Dipositing amount
def dep_Amount():
    ac =0
    ac_n= int(input("Enter Account Number : "))
    amount = int(input("Enter Amount : "))
    s = "select ac_balance from bank where ac_n='%d'"%(ac_n)
    c.execute(s)
    for data in c.fetchall():
        ac = data[0]
    total_amount = ac+amount
    s1 = "update bank set ac_balance='%d' where ac_n='%d'"%(total_amount,ac_n)
    r=c.execute(s1)
    if(r!=0):
        print("Record Updated : ",total_amount)
    else:
        print("Record Not Updated")
    con.commit()

#Amount withdraW
def Withdraw_Amount():
    ac = 0
    ac_n = int(input("Enter Account Number : "))
    amount = int(input("Enter Amount : "))
    s = "select ac_balance from bank where ac_n='%d'" % (ac_n)
    c.execute(s)
    for data in c.fetchall():
        ac = data[0]
    total_amount = ac - amount
    s1 = "update bank set ac_balance='%d' where ac_n='%d'" % (total_amount, ac_n)
    r = c.execute(s1)
    if (r != 0):
        print("Record Update : ",total_amount)
    else:
        print("Record Not Update")
    con.commit()

#Deleting account
def clos_ac():
    ac_n=int(input("Enter Account Number that you want to delete: "))
    s ="DELETE FROM bank WHERE ac_n='%d'"%(ac_n)
    c.execute(s)
    qry = "select * from bank"
    c.execute(qry)
    for data in c.fetchall():
        print("Acc_No ", "Name", "Password", "Balance" ,"Type\n",data[0], data[1],data[2],data[3],data[4])
    con.commit()

# Modifying value of account such as user name || bank balance || reset password and extra
def mod_acc():
    ap=0
    while(ap!=5):
        ap=int(input(("What is it you want to modify:\n1. Change name:\n2. update Bank balance \n3. Reset password\n4. Modify Bank type \n5.Exit\n")))

        if(ap == 1):
            ac_n=int(input("Enter Account Number whose name is to be used:"))
            a=input("New Name:")
            s1="UPDATE bank SET name = '%s' WHERE ac_n = '%d';"%(a,ac_n)
            r=c.execute(s1)

            if(r!=0):
                print("Record Update")
            else:
                print("Record Not Update")
            con.commit()

        elif(ap == 2):
            ac_n=int(input("Enter Account Number whose balance is to be changed:"))
            a=int(input("New balance:"))
            s1="UPDATE bank SET ac_balance = '%d' WHERE ac_n = '%d';"%(a,ac_n)
            r=c.execute(s1)
            if(r!=0):
                print("Record Update")
            else:
                print("Record Not Update")
            con.commit()

        elif(ap == 3):
            ac_n=int(input("Enter Account Number whose password is to be changed:"))
            a=input("New password:")
            s1="UPDATE bank SET password = '%s' WHERE ac_n = '%d';"%(a,ac_n)
            r=c.execute(s1)
            if(r!=0):
                print("Record Update")
            else:
                print("Record Not Update")
            con.commit()

        elif(ap == 4):
            ac_n=int(input("Enter Account Number whose type is to be changed:"))
            a=input("New type:")
            s1="UPDATE bank SET ac_t = '%s' WHERE ac_n = '%d';"%(a,ac_n)
            r=c.execute(s1)
            if(r!=0):
                print("Record Update")
            else:
                print("Record Not Update")
            con.commit()

def Bank():
    print("BANK's Account MANAGEMENT SYSTEM : ")
    while(True):
        op = int(input("Main Menu : \n1. Create New Account\n2. Show All Account\n3. Balance Enquery \n4. Deposit Amount \n5. Withdraw Amount\n6.Closing Account\n7.Modify an Account \n8.Exit \nSelect Your Option : \n"))
        if(op == 1):
            Create_Account()
        elif(op == 2):
            show_Record()
        elif(op == 3):
            Balance_Enc()
        elif(op == 4):
            dep_Amount()
        elif(op == 5):
            Withdraw_Amount()
        elif(op == 6):
            clos_ac()
        elif(op == 7):
            mod_acc()
        elif(op == 8):
            break
Bank()