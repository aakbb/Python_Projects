print("""
    ***************************
    User's Login Panel
    ***************************
      """)

sys_users_name = "ayse.akbb"
sys_name = "Ayse AKBABA"
sys_password = "123456"

username = input("User Name: ")
password = input("Password: ")

if sys_users_name != username and sys_password == password:
    print("İnvalid Username!")
elif sys_users_name == username and sys_password != password:
    print("Invalid Password!")
elif sys_users_name != username and sys_password != password:
    print("Invalid Username and Password!")
else:
    print("Logged in. Welcome {} :)".format(sys_name))