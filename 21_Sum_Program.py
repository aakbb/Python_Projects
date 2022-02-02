print("""
      *************************
      Welcome to Sum Program
      *************************
      This program adds the numbers you enter until you press q
      when you press the q, that will show the result
      q for quit
      """)

i = 0
sum =0
while True:
    n = input("Number: ")
    if n == "q":
        break
    
    n = int(n)
    sum += n
    
print("Sum = {}".format(sum))