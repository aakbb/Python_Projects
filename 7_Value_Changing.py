print("\nWelcome to Value Changing Program")

a= float(input("A:"))
b= float(input("B:"))

print("Before the Changing:\nA={}\nB={}".format(a,b))
a,b = b,a

print("After the Changing:\nA={}\nB={}".format(a,b))
