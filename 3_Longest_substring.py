# Brute force: my solution
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
        if len(temp) > maxlen:
            maxlen = len(temp)
    return maxlen

# print(lengthOfLongestSubstring(s1))

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
