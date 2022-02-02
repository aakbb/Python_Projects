"""
İkinci dereceden bir denklemin genel formülü :
        ax^2 + bx +c =0
    formatındadır

Bu denklemin köklerini ise deltayı hesaplayarak buluruz
delta = b^2 - 4*a*c

eğer delta değeri sıfırdan büyükse : birbirinden farklı iki kök vardır ve :
    r1 = (-b + delta** 0.5)/2
    r2 = (-b - delta** 0.5)/2

eğer delta değeri sıfıra eşitse : birbirine eşit iki kök vardır ve :
    r1 = r2 = (-b)/2*a

eğer delta değeri sıfırdan küçükse : reel kök yoktur

"""

print("\nWelcome to Root Finder Program")
print("----------------------------------------")
print("Please enter the coefficients")

a = int(input("\ta= "))
b = int(input("\tb= "))
c = int(input("\tc= "))

delta = b**2 - (4*a*c)

if delta>0:
    r1 = (-b + delta** 0.5)/2
    r2 = (-b - delta** 0.5)/2
    print("Roots:\nr1= {}\nr2= {}".format(r1 , r2))
elif delta == 0:
    r1 = r2 = (-b)/(2*a)
    print("Roots:\nr1= {}\nr2= {}".format(r1 , r2))
else:
    print("No root in real numbers!")
