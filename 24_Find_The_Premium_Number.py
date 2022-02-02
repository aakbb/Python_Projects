#Girilen sayının asal sayı olup olmadığını bulan programdır
#Asal sayı sadece bire ve kendisine bölünebilen sayılardır.
print("""****************
Bir sayının asal olup olmadığını bulma

Programdan çıkmak için 'q' ya basın.
****************
""")    

def isPremiumNumber(number):
    for i in range(2, number):
        if (number%i ==0):
            return False
    return True

        
while True:
    number = input("Number: ")
    if (number == "q"):
        print("Quiting the Program...")
        break
    number = int(number)
    
    if (number ==1):
        print(number , " is not a Premium Number")
    elif (number == 2):
        print(number , " is a Premium Number")
    else:
        if isPremiumNumber(number):
            print(number , " is a Premium Number")
        else:
            print(number , " is not a Premium Number")