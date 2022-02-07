'''
Return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? 
This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string.

Input: haystack = "hello", needle = "ll"
Output: 2
Input: haystack = "aaaaa", needle = "bba"
Output: -1
Input: haystack = "", needle = ""
Output: 0

'''

def strStr(haystack: str, needle: str):
    if needle not in haystack:
        return -1
    elif needle == "":
        return 0
    else:
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                count = 1
                while count<len(needle):
                    if haystack[i+count] == needle[0+count]:
                        count += 1
                    else:
                        break
                if count == len(needle):
                    return i

haystack = "hello"
needle = "ll"
print(strStr(haystack, needle))

haystack = "mississippi"
needle = "issip"
print(strStr(haystack, needle))

# haystack = "aaaaa"
# needle = "bba"
# print(strStr(haystack, needle))
# haystack = ""
# needle = ""
# print(strStr(haystack, needle))