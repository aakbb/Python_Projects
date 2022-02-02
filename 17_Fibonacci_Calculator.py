""""
Fibonacci, sayıları yeni bir terimi önceki iki sayının toplamından elde eden bir dizidir.
1 1 2 3 5 8 13 21 34 55 ...
Programın amacı for döngüsü yardımıyla Fibonacci sayısını hesaplayabilmek
"""

fb1 =1
fb2 =1
fibonacci = [fb1 , fb2]
n = int(input("Which Fibonacci term you want to find: "))

for i in range(n-2):
    fb1 , fb2 = fb2 , fb1+fb2
    fibonacci.append(fb2)

print(fibonacci)
print("F{} = {}".format(n , fb2))
