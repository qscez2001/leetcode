# Brute force: my solution O(n^3)
s1 = "bcaabcbb"
s2 = "bbbbb"
s3 = "pwwkew"

def lengthOfLongestSubstring(s):
    maxlen = 0
    for i in range(len(s)):
        temp = []
        temp.append(s[i])
        for j in range(i+1, len(s)):
            if s[j] not in temp:
                temp.append(s[j])
            else:
                break
        # print(temp)
        if len(temp) > maxlen:
            maxlen = len(temp)
    return maxlen

# brute force
from collections import defaultdict
def lengthOfLongestSubstring(self, s: str) -> int:
    
    def check(start, end):
        chars = defaultdict(lambda: 0)
        for i in range(start, end + 1):
            c = s[i]
            chars[c] += 1
            if chars[c] > 1:
                return False
        return True
    
    res = 0
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            # check if string duplicate
            if check(i, j):
                res = max(res, j-i+1)
    return res

print(lengthOfLongestSubstring(s1))

# others (slide window)
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    
    str_list = []
    max_length = 0
    
    for x in s:
        if x in str_list:
            str_list = str_list[str_list.index(x)+1:]
            # print(str_list)
            
        str_list.append(x)    
        # print(str_list)
        max_length = max(max_length, len(str_list))
        
    return max_length

# print(lengthOfLongestSubstring(s1))

# fastest solution
def lengthOfLongestSubstring(s):
    dicts = {}
    maxlength = start = 0
    for i, value in enumerate(s):
        if value in dicts:
            sums = dicts[value] + 1
            if sums > start:
                start = sums
        num = i - start + 1
        if num > maxlength:
            maxlength = num
        dicts[value] = i
    return maxlength

print(lengthOfLongestSubstring(s1))
