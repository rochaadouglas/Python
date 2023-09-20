from function_factorial import factorial
def NP(num, mult):
    num_n = num
    num_p = mult
    result = num_n / (num_p *(num_n - num_p))
    return factorial(num_n, num_p)
test = NP(3, 2)
print(test)