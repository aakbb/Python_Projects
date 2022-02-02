#Türkçe karşılığı haritalamak da olsa yazılım dilinde bununla bir alakası yoktur
#Maping yazılımda eşitlemek anlamına gelir.
#Mesela bizim üç verili bir k datamız olsun. Bu datayı bozmadan üstünde değişiklik yapmak istiyorsan maping yaparsın.
#Kısacası bir veriyi ya da bilgiyi olduğu gibi başka bir yere atama ,kopyalama, işlemidir.

numbers =[1,2,3,4,5]
squart =[]
for i in numbers:
    squart.append(i*i)
print(squart)
#yukarıdaki işlem yerine maping yaparsak:

squart = list(map(lambda number : number**2 , numbers))
#bu işlemin anlamı:
#numbers listesi içinde her bir sayı için sayının karesini al ve liste biçiminde yaz.