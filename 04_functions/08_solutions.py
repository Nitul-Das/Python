def print_kwargs(**kwargs): # syntax allows you to pass a variable number of keyword arguments to the function.
    for key, value in kwargs.items():
        print(f"{key}: {value}") # f allows to embed expressions inside string literals, using curly braces {}.

print_kwargs(name="jett", power = "dash")
print_kwargs(name="Pheonix")
print_kwargs(name="Sage", power="heal", ultimate="revive")
