
students = ["Engin" , "Derin" , "Salih" , "Ali" , "Ayse"]

student = open("Students.txt" , "a") #Oluşturulan dosyanın türünü yazmazsan default'u metin dosyası şeklinde olur.
for i in students:
    student.write(i)
    student.write("\n")
student.close()