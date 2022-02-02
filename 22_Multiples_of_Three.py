""""
Bu program 1 ile 100 aralığındaki üçün katları olan değerleri continue ifadesi ile yazdırır.

"""

for i in range(1,101):
    if i % 3 != 0:
        continue
    print(i)