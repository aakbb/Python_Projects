print("\nWelcome to Registration Program\n----------------------------------------")

name=input("Name: ")
surname=input("Surname: ")
phoneNumber=input("Phone Number: ")

information = [name ,surname , phoneNumber]

print("\nThe person is being registered...\nRegistered\n")
print("Showing the Personal İnformations:")
print("Name: {}\nSurname: {}\nPhone Number: {}\n".format(information[0] , information[1] , information[2]))

