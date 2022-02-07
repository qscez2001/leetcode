'''
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), 
which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of groups so that 

each group is a contiguous section all of the same character. 
Then for each group, say the number of characters, then say the character. 
To convert the saying into a digit string, replace the counts with a number and concatenate every saying.

For example, the saying and conversion for digit string "3322251":
Given a positive integer n, return the nth term of the count-and-say sequence.

countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
'''

def countAndSay(n):
    if n == 1:
        return '1'

    else:
        output_of_last = countAndSay(n-1)

        if len(output_of_last) == 1:
            return '11'
        else:
            my_dict = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '0': 0} 
 
            my_str = ""  

            for i in range(len(output_of_last)):
                if i == 0:
                    my_dict[output_of_last[i]] += 1
                else:
                    if output_of_last[i] == output_of_last[i-1]:
                        my_dict[output_of_last[i]] += 1
                    else:
                        my_str += str(my_dict[output_of_last[i-1]]) + str(output_of_last[i-1])
                        my_dict[output_of_last[i-1]] = 0
                        my_dict[output_of_last[i]] = 1 

            my_str += str(my_dict[output_of_last[i]]) + str(output_of_last[i])
            return my_str

n = 1
# Output: "1" Explanation: This is the base case.
print(countAndSay(n))
n = 2
print(countAndSay(n))
n = 3
print(countAndSay(n))
n = 4
print(countAndSay(n))
n = 5
print(countAndSay(n))
'''
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
'''