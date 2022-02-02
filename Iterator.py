#Ittratorlerin genel mantığı bir liste , set ya da dictinary de elemanları tek tek gezmeye yarar.
#her bir iterate işleminde yapının bir elemanını tarar.
#for döngüsü de bir iterator'dır.

city =["Ankara" , "İstanbul" , "Sivas"]
iteratorum = iter(city)

print(next(iteratorum))
print(next(iteratorum))
print(next(iteratorum))

#Bunun yerine daha kolay olan for döngüsünü kullanırız.

print("************")
for i in city:
    print(i)