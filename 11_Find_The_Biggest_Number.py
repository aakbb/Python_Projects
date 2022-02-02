print("""
      ************************************************
      Welcome to Finding The Biggest Number Program
      ************************************************
      """)
n1 = int(input("number1: "))
n2 = int(input("number2: "))
n3 = int(input("number3: "))

if n1>n2 and n1>n3:
    print("The Biggest Number is {}".format(n1))
elif n2>n1 and n2>n3:
    print("The Biggest Number is {}".format(n2))
else:
    print("The Biggest Number is {}".format(n3))