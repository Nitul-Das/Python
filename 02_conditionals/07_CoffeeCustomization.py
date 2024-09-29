order_size = input("give order size: ")
extra_short = input("Add or Dont Add: ").lower()

if extra_short == "add":
    order = order_size + " coffe with an extra shot"
else:
    order = order_size +" coffe"
print("Your order :", order)