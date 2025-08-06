#  ATM SIMULATOR - JSR BANK (IF-ELSE VERSION)

# Stored credentials and account info
username = "jaswinder"
password = "1234"
account_holder = "Jaswinder Singh"
bank_name = "JSR BANK"
account_number = "123456789012"
ifsc = "JSRB0001234"
mobile = "9876543210"
balance = 10000

# -------- LOGIN --------
print("----- Welcome to JSR BANK ATM -----")
input_user = input("Enter username: ")
input_pass = input("Enter password: ")

if input_user == username and input_pass == password:
    print("Login successful!\n")

    while True:
        print("\n----- MENU -----")
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Account Info")
        print("5. Change Password")
        print("6. Update Mobile Number")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            print(f"Your current balance is: ₹{balance}")

        elif choice == "2":
            amount = int(input("Enter amount to withdraw: ₹"))
            if amount > balance:
                print("Insufficient balance.")
            else:
                balance -= amount
                print(f"₹{amount} withdrawn successfully.")

        elif choice == "3":
            amount = int(input("Enter amount to deposit: ₹"))
            balance += amount
            print(f"₹{amount} deposited successfully.")

        elif choice == "4":
            print("----- ACCOUNT INFO -----")
            print(f"Account Holder: {account_holder}")
            print(f"Bank Name: {bank_name}")
            print(f"Account Number: {account_number}")
            print(f"IFSC Code: {ifsc}")
            print(f"Mobile Number: {mobile}")

        elif choice == "5":
            old = input("Enter old password: ")
            if old == password:
                new = input("Enter new password: ")
                password = new
                print("Password changed successfully.")
            else:
                print("Incorrect old password.")

        elif choice == "6":
            new_mobile = input("Enter new 10-digit mobile number: ")
            if new_mobile.isdigit() and len(new_mobile) == 10 and new_mobile[0] in ['9', '8', '7', '6']:
                mobile = new_mobile
                print("Mobile number updated.")
            else:
                print("Invalid mobile number.")

        elif choice == "7":
            print("Thank you for using JSR BANK ATM. Goodbye!")
            break

        else:
            print("Invalid option. Please choose from 1 to 7.")

else:
    print("Login failed. Invalid username or password.")
