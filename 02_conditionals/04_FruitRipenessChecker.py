fruit = input("Give a fruit: ")
color = input("Give a color: ")

if fruit == "Banana":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("Overripe")
    else:
        print("Unknown color")
else:
    print("Fruit not recognized")
