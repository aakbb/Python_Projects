print("""***********************************
      Welcome to Basic Calculator Program
      
      Options:
      1.Sum
      2.Extraction
      3.Multiplication
      4.Divide
      ***********************************
      """)

choose = int(input("Choose your option's number:"))
number1 = float(input("Enter the number1:"))
number2 = float(input("Enter the number2:"))
if choose == 1:
    print("{} + {} = {}".format(number1 , number2 , number1 + number2))
elif choose ==2:
    print("{} - {} = {}".format(number1 , number2 , number1 - number2))
elif choose ==3:
    print("{} * {} = {}".format(number1 , number2 , number1 * number2))
elif choose ==4:
    print("{} / {} = {:.2f}".format(number1 , number2 , number1 / number2))
else:
    print("Incorrect Option Number!")