def sum_all(*args):  #can pass multiple arguments
    for i in args:
        print(i * 2)
    return sum (args)

print(sum_all(1,2,3))
# print(sum_all(1,2,3,4,6))
# print(sum_all(1,2,3,4,5,6,7,8))