print("\nWelcome to Fuel-Mileage Calculator")

fuel = float(input("Please enter the how much the car burns per kilometer = "))
mileage = float(input("Enter the how many kilometers did you travel = "))

amount = fuel*mileage

print("You should pay {:.2f} $ for this travel".format(amount))