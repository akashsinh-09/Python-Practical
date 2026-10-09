print("Welcome to the Interactive Personal Data Collector! \n")


firstname = input("Please enter your name:")
age = int(input("Please enter your age: "))
height= float(input("Please enter your height in meters:"))
number=int(input("Please enter your favourite number:"))

print("Thank you ! Here is the information we collected: \n")

print("Name:", firstname, type(firstname))
print("Age:", age, type(age))
print("Height:", height, "meters", type(height))
print("Favourite Number:", number, type(number))

print("Your birth year is approximately:",2026 - age,"(based on your age of",age,")\n")

print("Thank you for using the Interactive Personal Data Collector.Goodbye!")

