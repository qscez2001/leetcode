def isPalindrome(self, x: int) -> bool:
    x = str(x)
    rev = x[::-1] 

    # Checking if both string are equal or not 
    if (x == rev): 
        return True
    return False