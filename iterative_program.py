import random

def factorial(n):
    assert(n > 0)
    result = 1

    for i in range(1, n+1):
        result *= i
    return result

def recursive(n):
    assert(n>0)
    # Base Case 
    if n ==1 :
        return 1
    else:
        return n * factorial(n -1) 

# Example of Infinite Recursion
def infinite(n):
    if n == 1:
        return 0
    return n * infinite(n+1)


# def change(amount):
#     assert(amount>=8)

#     if amount == 8:
#         return [3, 5]
#     if amount == 9:
#         return [3, 3, 3]
#     if amount == 10:
#         return [5, 5]

#     # return takes place of variable
#     # so amount = return value
#     coins = change(amount - 3)
#     coins.append(3)
#     return coins

# Develop a Python method change(amount) that for any integer amount in the range from 
# 24 to 1000 returns a list consisting of numbers 5 and 7 only, 
# such that their sum is equal to amount. For example, change(28) 
# may return [7, 7, 7, 7], while change(49) may return [7, 7, 7, 7, 7, 7, 7] or 
# [5, 5, 5, 5, 5, 5, 5, 7, 7] or [7, 5, 5, 5, 5, 5, 5, 5, 7].
# To solve this quiz, implement the method change(amount) on your machine, 
# test it on several inputs, and then paste your code in the field below and 
# press the submit quiz button. Your submission should contain the change method only 
# (in particular, make sure to remove all print statements).
def change(amount):
    assert(24 <= amount <= 1000)

    if amount == 24:
        return [5, 5, 7, 7]
    if amount == 25:
        return [5, 5, 5, 5, 5]
    if amount == 26:
        return [5, 7, 7, 7]
    if amount == 27:
        return [5, 5, 5, 5, 7]
    if amount == 28:
        return [7, 7, 7, 7]
    if amount == 29:
        return [5, 5, 5, 7, 7]
    if amount == 30:
        return [5, 5, 5, 5, 5, 5]
    if amount == 31:
        return [5, 5, 7, 7, 7]
    if amount == 32:
        return [5, 5, 5, 5, 5, 7]
    if amount == 33:
        return [5, 7, 7, 7, 7]
    
    result = change(amount - 7)
    result.append(7)
    return result

print(factorial(10))
print(recursive(10)) 
# print(infinite(3))
print(change(random.randint(24, 1000)))
