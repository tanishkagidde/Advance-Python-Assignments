def outer_func(x):
    def inner_func(y):
        return x*y
    return inner_func
multiply_ten = outer_func(10)
print(multiply_ten(5))

'''
OUTPUT: 50
'''
