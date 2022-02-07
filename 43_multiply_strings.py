'''
Given two non-negative integers num1 and num2 represented as strings, 
return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the 
inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
'''

def multiply(num1, num2):
    if num1 == "0" or num2 == "0":
        return "0"

    list1 = [] 
    for ele in num1: 
        list1.extend(ord(num) - ord('0') for num in ele) 
    list2 = [] 
    for ele in num2: 
        list2.extend(ord(num) - ord('0') for num in ele)
    
    temp1 = 0
    digits_num1 = len(list1) - 1
    for i in range(len(list1)):
        temp1 = temp1 + list1[i] * pow(10, digits_num1-i)
    # print(temp1)
    temp2 = 0
    digits_num1 = len(list2) - 1
    for i in range(len(list2)):
        temp2 = temp2 + list2[i] * pow(10, digits_num1-i)
    # print(temp2)

    calculate = temp1*temp2
    # print(calculate)
    ans_list = []
    while calculate !=0 :    
        digit = calculate % 10 # 個位數
        ans_list.append(digit)
        calculate = calculate // 10
    # print(ans_list)
    asc_0 = 48
    ans_str = ""
    for ele in ans_list:
        ans_str = ans_str + chr(asc_0 + ele)
    ans_str = ans_str[::-1]
    # print(ans_str)
    return ans_str

num1 = "2"
num2 = "3"
multiply(num1, num2)
num1 = "123"
num2 = "456"
multiply(num1, num2)
