'''
Given a string s and a dictionary of strings wordDict, 
return true if s can be segmented into a space-separated sequence of 
one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
'''

# not solved
def wordBreak(s, wordDict):
    temp = s
    while temp:
        for w in wordDict:
            if temp.find(w) != -1:
                index = temp.find(w)
                temp = temp[:index] + temp[index+len(w):]
                print(temp)

        if temp == "":
            return True

        # False condition, break
        lenth = [len(w) for w in wordDict]
        count = 0
        for l in lenth:
            if len(temp) < l:
                count += 1
        if count == len(wordDict):
            return False

from functools import lru_cache 
def recursive(s, wordDict):
    temp = s
    if temp == "":
        return True
    for w in wordDict:
        if temp.find(w) != -1:
            index = temp.find(w)
            temp = temp[:index] + temp[index+len(w):]
            # print(temp)
        return recursive(temp, wordDict)


def wordBreak(s, wordDict):
    # @lru_cache
    if recursive(s, wordDict) == None:
        return False
    return True

from functools import lru_cache 
# brute force solution
# recursion with memorization
# Time complexity : O(n^3). Size of recursion tree can go up to n^2
 .
def wordBreak(s, wordDict):
    @lru_cache(None)
    def wordBreakMemo(s, word_dict, start):
        if start == len(s):
            return True
        for end in range(start + 1, len(s) + 1):
            print(s[start:end])
            # print(end)
            if s[start:end] in word_dict and wordBreakMemo(s, word_dict, end):
                return True
        return False

    return wordBreakMemo(s, frozenset(wordDict), 0)

# DP solution
'''
Time complexity : O(n^3). 
There are two nested loops, and substring computation at each iteration. 
Overall that results in O(n^3) time complexity.
'''
# The intuition behind this approach is that the given problem (s) can be divided into subproblems s1 and s2.
# If both the strings fulfill the criteria, we make dp[i] as true
def wordBreak(s, wordDict):
    word_set = set(wordDict)
    dp = [False] * (len(s) + 1)
    # we initialize the element dp[0] as true, since the null string is always present in the dictionary
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            print("i={}, j={}".format(i,j))
            print(dp)
            print(s[j:i])
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                
    print(dp)
    return dp[len(s)] # the last one

# s = "leetcode"
# wordDict = ["leet","code"]
# print(wordBreak(s, wordDict))

s = "applepenapple"
wordDict = ["apple","pen"]
print(wordBreak(s, wordDict))

# s = "catsandog"
# wordDict = ["cats","dog","sand","and","cat"]
# print(wordBreak(s, wordDict))

# s = "a"
# wordDict = ["b"]
# print(wordBreak(s, wordDict))


