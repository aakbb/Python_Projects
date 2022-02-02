from turtle import right


print("""
      ****************************
      Welcome to Login Panel
      ****************************
      """)
sys_username = "ayse.akbb"
sys_password = "12345"
user_information = "Ayse AKBABA"

right_of_entry = 3
i =0
while True:
    username = input("Username: ")
    password = input("Password: ")
    
    if sys_username != username and sys_password == password:
        print("Invalid Username. Please Try Again!")
        right_of_entry -=1
        print("Right of Entry: {}".format(right_of_entry))
    elif sys_username == username and sys_password != password:
        print("Invalid Password. Please Try Again!")
        right_of_entry -=1
        print("Right of Entry: {}".format(right_of_entry))
    elif sys_username != username and sys_password != password:
        print("Invalid Username and Password. Please Try Again!")
        right_of_entry -=1
        print("Right of Entry: {}".format(right_of_entry))
    else:
        print("Logged in. Welcome {}".format(user_information))
        break
    
    if right_of_entry ==0:
        print("End of your right of entry. Please Try Again in 24 hours")
        break