import math

# x! = x*(x-1)*(x-2)...*1
# 5! = 5*4*3*2*1 = 120

def factorial(num):
    # isinstance checks if the value of the variable is of the datatype
    # here, variable is 'num' and datatype is 'int'
    # so, if num is integer, and it is greater than or equal to zero(is positive), 
    # then only work will be done. Otherwise, Invalid will be shown
    if (isinstance(num, int) and num>=0):
        if (num==1 or num == 0):
            return 1
        if (num>=2): 
            return num*factorial(num-1)
    else:
        return 'Invalid'
    
    
# factorial(5) -> 5*factorial(4) -> 5*4*factorial(3) ->
# 5*4*3*factorial(2) -> 5*4*3*2*factorial(1) => 5*4*3*2*1 = 120
    
print(factorial(5))
print(factorial('hj'))
print(factorial(-5))

def loopFactorial(x):
    result = 1
    for i in range(1,x+1): #1,2,....,x
        result *= i
    return result
# x*=i -> x = x*i
# result = 1*1 -> 1*2 -> 2*3 -> 6*4 -> 24*5 -> 120
print(loopFactorial(5))
print(math.factorial(5))