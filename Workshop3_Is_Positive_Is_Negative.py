#Kullanıcıdan alınan bir sayının pozitif mi negatif mi olduğunu söyleyen program

number = int(input("Please enter a number= "))

if number > 0:
    print(str(number) + " is Possitive")
elif number == 0:
    print(str(number) + " is Notr")
else:
    print(str(number) + " is Negative")