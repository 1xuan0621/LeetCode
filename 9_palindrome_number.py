# def isPalindrome(x: int):
#     if x < 0 or (x > 0 and x % 10 == 0):
#         return False

#     result = 0
#     while result < x:
#         result *= 10
#         result += x % 10
#         x //= 10
#     return result == x or result //10 == x

# print(isPalindrome(11))
def fk(x):
    if x < 0 or (x > 0 and x%10 == 0):
        return False
        
    result = 0
    while x > result:
        result = result * 10 + x % 10
        x = x // 10
        
    return True if (x == result or x == result // 10) else False