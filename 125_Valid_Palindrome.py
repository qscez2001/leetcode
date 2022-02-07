'''
Given a string, determine if it is a palindrome, 
considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, 
we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
'''

def isPalindrome(s):
    s = s.lower()
    alphanumeric = [c for c in s if c.isalnum()]
    
    head = 0
    tail = len(alphanumeric) - 1
    medium = len(alphanumeric) // 2
    while head != medium:
        if alphanumeric[head] != alphanumeric[tail]:
            return False
        else:
            head += 1
            tail -=1
    return True

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
s = "race a car"
# print(isPalindrome(s))