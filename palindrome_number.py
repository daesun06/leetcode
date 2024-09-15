
def isPalindrome(self, x: int) -> bool:
    if x < 0:
        return False
    divider = 1
    while x>= 10 * divider:
        divider *= 10

    while x != 0:
        rightd = x % 10 
        leftd = x // divider

        if leftd != rightd:
            return False

        x = (x % 10) // 10
        divider = divider / 100
    return True
    


print(isPalindrome())