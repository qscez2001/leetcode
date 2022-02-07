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
    
# DP solution
def longestPalindrome(self, s):
        longest_palindrom = ''
        dp = [[0]*len(s) for _ in range(len(s))]
        #filling out the diagonal by 1
        for i in range(len(s)):
            dp[i][i] = True
            longest_palindrom = s[i]
			
        # filling the dp table
        for i in range(len(s)-1,-1,-1):
				# j starts from the i location : to only work on the upper side of the diagonal 
            for j in range(i+1,len(s)):  
                if s[i] == s[j]:  #if the chars mathces
                    # if len slicied sub_string is just one letter if the characters are equal, we can say they are palindomr dp[i][j] =True 
                    #if the slicied sub_string is longer than 1, then we should check if the inner string is also palindrom (check dp[i+1][j-1] is True)
                    if j-i ==1 or dp[i+1][j-1] is True:
                        dp[i][j] = True
                        # we also need to keep track of the maximum palindrom sequence 
                        if len(longest_palindrom) < len(s[i:j+1]):
                            longest_palindrom = s[i:j+1]
                
        return longest_palindrom

print(longestPalindrome(s3))