def impure_squared(number):
    result = number ** 2
    print('The square of', number, 'is', result)
    return result

def pure_squared(number):
    return number ** 2

#The pure function does not have any side effects, it only returns the squared value without printing anything. The impure function, on the other hand, has a side effect of printing the result to the console.
