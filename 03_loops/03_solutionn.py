# Multiplication Table Printer
number = int(input("give a number:"))

for i in range(1, 11):
    if i == 5:
        continue
    print(number, 'x', i, '=', number * i)

