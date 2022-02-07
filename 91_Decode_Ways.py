'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, 
determine the total number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.

Example 1:

Input: s = "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:

Input: s = "0"
Output: 0
Explanation: There is no character that is mapped to a number starting with '0'. 
We cannot ignore a zero when we face it while decoding. 
So, each '0' should be part of "10" --> 'J' or "20" --> 'T'.

Example 4:

Input: s = "1"
Output: 1
'''
# not solved 
def numDecodings(s):
    print(len(s))
    if s == "0":
        return 0
    elif len(s) == 1:
        return 1
    elif s == "10" or s == "20":
        return 1
    elif len(s) == 2 and int(s) < 27:
        return 2
    else:
        return numDecodings(s[0:1]) + numDecodings(s[1:])

# dp and dfs
# https://leetcode.com/problems/decode-ways/discuss/608268/Python-Thinking-process-diagram-(DP-%2B-DFS)
def numDecodings(s:str):
    from functools import lru_cache 

    if len(s) == 0 or s is None:
        return 0

    @lru_cache(maxsize=None)
    def dfs(string):
        print(string)
        if len(string)>0:
            if string[0] == '0':
                return 0
        if string == "" or len(string) == 1:
            return 1
        if int(string[0:2]) <= 26:
            first = dfs(string[1:])
            second = dfs(string[2:])
            return first+second
        else:
            return dfs(string[1:])

    result_sum = dfs(s)

    return result_sum

# s = "12"
# print(numDecodings(s))
# s = "226"
# print(numDecodings(s))
s = "0"
print(numDecodings(s))
s = "2221"
print(numDecodings(s))

