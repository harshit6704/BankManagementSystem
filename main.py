# main.py
import account_manage

def bank():
    print("BANK's Account MANAGEMENT SYSTEM : ")
    
    while True:
        print("Main Menu : ")
        print("1. Create New Account")
        print("2. Show All Account")
        print("3. Balance Enquiry")
        print("4. Deposit Amount")
        print("5. Withdraw Amount")
        print("6. Closing Account")
        print("7. Modify an Account")
        print("8. Exit")
        
        op = int(input("Select Your Option : "))
        
        if op == 1:
            account_manage.create_account()
        elif op == 2:
            account_manage.show_records()
        # Add other options similarly
        elif op == 8:
            break

if __name__ == "__main__":
    bank()