#Javada inherit etmek için extend keyini kullanırdık
#Python'da ise class isminin yanına parantez açıp inherit etmek istediğimiz class'ın ismini yazıyoruz.

class Person:
    def __init__(self , name , surname , age):
        self.name = name
        self.surname = surname
        self.age = age

class Workers(Person):
    def __init__(self, name, surname, age , salary):
        super().__init__(name, surname, age)
        self.salary = salary

class Customer(Person):
    def __init__(self, name, surname, age , creditCardNumber):
        super().__init__(name, surname, age)
        self.creditCardNumber = creditCardNumber

person = Person("Ayşe" , "Akbaba" , 19)
print(person.name)
ahmet = Workers("Ahmet" , "Akyıldız" , 24 , 2875)
print(ahmet.salary)