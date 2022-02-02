#Bir sayının tam bölenlerini fonksiyon yardımıyla bulan bir programdır.

def exactDivisors(number):
    divisors = list()
    for i in range(1,number+1):
        if number % i == 0:
            divisors.append(i)
    print(divisors)
        
print("""
      **********************************
      Welcome to Find the Exact Program
      **********************************
      Program will continue to work until you press 'q'
      q for quit
      """)

while True:
    number = input("Number: ")
    if number == "q":
        print("Quiting the Program...")
        break
    else:
        number = int(number)
        exactDivisors(number)
            