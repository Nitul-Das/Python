number = int(input('give a number'))

prime_num= True
if number > 1:
    for i in range( 2, number):
        if number % i == 0:
            is_prime = False
            break

print(prime_num)