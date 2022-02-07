'''
Given a non-negative integer numRows, 
generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

def generate(numRows: int):
    ans = []
    for i in range(numRows):
        # print(ans, i)
        newlist = []
        if i < 2:
            for j in range(i+1):
                newlist.append(1)
            ans.append(newlist)
        else:
            newlist.append(1)
            prev_list = ans[i-1]
            for j in range(len(prev_list) - 1):
                item = prev_list[j] + prev_list[j+1]
                newlist.append(item)
            newlist.append(1)
            ans.append(newlist)

    return ans

numRows = 5
print(generate(numRows))