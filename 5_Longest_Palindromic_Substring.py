s1 = "babad"
s2 = "cbbd"
s3 = "abcda"

def reverse(s): 
    return s[::-1] 
  
def isPalindrome(s): 
    # Calling reverse function 
    rev = reverse(s) 
  
    # Checking if both string are equal or not 
    if (s == rev): 
        return True
    return False

def longestPalindrome(s):
    maxlen = 0
    sub = ""
    for i in range(len(s)):
        temp = ""
        temp = temp + s[i]
        for j in range(i+1, len(s)):
            temp = temp + s[j]
            if isPalindrome(temp):
                if len(temp) >= maxlen:
                    maxlen = len(temp)
                    sub = temp
    return sub

# my solution
def longestPalindrome(s):
    maxlen = 0
    sub = ""
    for i in range(len(s)):
        temp = ""
        temp = temp + s[i]
        if len(s) == 1:
            return s
        for j in range(i+1, len(s)):
            temp = temp + s[j]
            rev = temp[::-1]
            if temp == rev:
                if len(temp) >= maxlen:
                    maxlen = len(temp)
                    sub = temp
            # print(temp)
    if sub == "" and len(s) != 0:
        sub = s[0]
    return sub

# others solution:faster just a little
def longestPalindrome(self, s: str) -> str:
    m = ''  # Memory to remember a palindrome
    for i in range(len(s)):  # i = start, O = n
        for j in range(len(s), i, -1):  # j = end, O = n^2
            if len(m) >= j-i:  # To reduce time
                break
            elif s[i:j] == s[i:j][::-1]:
                m = s[i:j]
                break
        return m

print(longestPalindrome(s3))