'''
Given a non-empty array of decimal digits representing a non-negative integer, 
increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, 
and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself. 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

Example 3:

Input: digits = [0]
Output: [1]
'''

def plusOne(digits):
    # print(digits[-1])  
    digits[-1] += 1
    # loop backwards
    for i in range(len(digits)-1, -1, -1):
        # print(i)
        if i == 0 and digits[i] == 10:
            digits.append(0)
            digits[i] = 1
            break

        if digits[i] == 10:
            digits[i] = 0
            digits[i-1] += 1

    # print(digits) 
    return digits

digits = [1,2,3]
print(plusOne(digits))
digits = [4,3,2,1]
print(plusOne(digits))
digits = [0]
print(plusOne(digits))
digits = [9]
print(plusOne(digits))