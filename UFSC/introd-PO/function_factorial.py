def factorial(number):
    fact = number
    mult = fact - 1
    while mult > 1:
        fact = fact * mult
        mult -= 1
    return fact
test = factorial(5)
print(test)