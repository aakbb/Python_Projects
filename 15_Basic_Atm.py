print("""
      *************************************
      Welcome to ATM Machine
      *************************************
      Options:
      1.Balance Inquiry
      2.Withdraw Money
      3.Deposit Money
      Q.For Quiting
      *************************************
      """)

balance = 4250

while True:
    choose = input("Enter the Your Option's Number: ")
    if choose == "1":
        print("There is {} Turkish liras in your balance.".format(balance))
    elif choose == "2":
        amount = int(input("Amount of Money to be Withdrawn: "))
        if balance - amount < 0:
            print("Insufficient Balance!Current Balance is {} Turkish Liras".format(balance))
        else:
            balance -= amount
            print("Money was Taken. New Balance: {} Turkish Liras".format(balance))
    elif choose == "3":
        add_amount = int(input("Amount to be Added: "))
        balance += add_amount
        print("New Balance: {} Turkish Liras".format(balance))
    elif choose == "Q":
        print("Quiting the Program...")
        break
    else:
        print("Invalid Option Number. Please Try Again")