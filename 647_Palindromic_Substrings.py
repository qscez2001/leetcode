# my solution
def countSubstrings(self, s):
    """
    :type s: str
    :rtype: int
    """
    def is_palindrome(s):
        rev = s[::-1]
        if s == rev:
            return True
        return False
    
    sub = []
    for i in range(len(s)+1):
        for j in range(i+1, len(s)+1):
            sub.append(s[i:j])
    print(sub)
    c = 0
    for s in sub:
        if is_palindrome(s):
            c += 1
    
    return c
# Approach #2: Dynamic Programming
'''
Intuition

Approach #1 spent a lot of time checking if a particular substring is a palindrome. 
What if we could speed up this check, by say, reusing previously calculated results? 
Turns out that checking whether a string is a palindrome or not, is a good candidate for dynamic programming!

It displays the two, necessary characteristics of a dynamic programming problem:
1. Optimal substructure
2. Overlapping sub-problems

Algorithm

Here's the simple framework for our dynamic programming solution:

1. Define the dynamic programming state. This is the result that gets reused in further computations.

Let's define our state dp(i, j), which tells us whether the substring 
composed of the ith to the jth characters of the input string, is a palindrome or not.

Thus, the answer to our problem lies in counting all substrings whose state is true.

2. Identify the base cases. There are essentially two base-cases:

Single letter substrings are palindromes by definition. i.e. dp(i, i) = true
Double letter substrings composed of the same character are palindromes. 
i.e. dp(i,i+1) = true if s_i = s_{i+1} 
                false otherwise

3. Identify the optimal substructure. A string is considered a palindrome if:

Its first and last characters are equal, and
The rest of the string (excluding the boundary characters) is also a palindrome.
This optimal substructure can be formulated into a recurrence rule: 
dp(i,j) = true if dp(i+1, j-1) and (s_i = s_j)
         false otherwise

4. Identify overlapping sub-problems and compute them only once. 
The optimal substructure mentioned above ensures that the state for a string depends only on the state for a single substring. 
If we compute (and save) the states for all smaller strings first, larger strings can be processed by reusing previously saved states. 
The base cases that we have identified already define states for single and double letter strings. 
We can use those to compute states for three character (and subsequently larger) strings.

5. The answer is found by counting all states that evaluate true. 
Since each state tells whether a unique substring is a palindrome or not, 
counting true states provides us the number of palindromic substrings.

'''
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        count = 0

        dp = [[False for x in range(n)] for y in range(n)]
        
        # Base case: single letter substrings
        for i in range(n):
            dp[i][i] = True
            count += 1
        
        # Base case: double letter substrings
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                count += 1
        
        # All other cases: substrings of length 3 to n
        for k in range(3, n+1):
            for i in range(n-k+1):
                j = i+k-1
                if dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = True
                    count += 1

        return count

# https://leetcode.com/problems/palindromic-substrings/discuss/555333/Python-Dynamic-Programming-Solution
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        res = 0
        
        # create a matrix to store info about the substring 
        dp = [[0 for i in range(n)] for j in range(n)]
        
        # set single characters as palindromes
        idx = 0
        while idx < n:
            dp[idx][idx] = 1
            idx += 1
            res += 1
        
        # fill the matrix 
        # example1: "aaaaa"
        # [1, 1, 1, 1, 1]
        # [0, 1, 1, 1, 1]
        # [0, 0, 1, 1, 1]
        # [0, 0, 0, 1, 1]
        # [0, 0, 0, 0, 1]
        
        # example2: "cdaabaad"
        # [1, 0, 0, 0, 0, 0, 0, 0]
        # [0, 1, 0, 0, 0, 0, 0, 1]
        # [0, 0, 1, 1, 0, 0, 1, 0]
        # [0, 0, 0, 1, 0, 1, 0, 0]
        # [0, 0, 0, 0, 1, 0, 0, 0]
        # [0, 0, 0, 0, 0, 1, 1, 0]
        # [0, 0, 0, 0, 0, 0, 1, 0]
        # [0, 0, 0, 0, 0, 0, 0, 1]
        
        for col in range(1, len(s)):
            for row in range(col):
                
                # every two chars are palindromes as well
                if row == col - 1 and s[col] == s[row]:
                    dp[row][col] = 1
                    res += 1
                
                # to determine if substring is a palindrome you should know 
                # a) if the inner substring is the palindrome and
                # b) if the outer characters match
                elif dp[row + 1][col - 1] == 1 and s[col] == s[row]:
                    dp[row][col] = 1
                    res += 1
        
        # print matrix
        # for line in dp:
        #     print(line)
        
        return res