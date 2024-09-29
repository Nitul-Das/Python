age = int(input("enter age:"))
day = input("give a day:")

price = 12 if age >= 18 else 8 

if day == "wednesday":
    price = price - 2
print("Ticket price for you is $",price)

