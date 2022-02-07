# Time Limit Exceeded
def maxArea(height):
    
    max_area = 0
    for i in range(len(height)):
        for j in range(i+1, len(height)):
            length = min(height[i],height[j])
            width = j-i
            area = length*width
            if area > max_area:
                max_area = area

    return max_area

# O(n) solution, others
# Approach 2: Two Pointer Approach
'''
The intuition behind this approach is that the area formed between the lines will always be limited by the height of the shorter line. Further, the farther the lines, the more will be the area obtained.

We take two pointers, one at the beginning and one at the end of the array constituting the length of the lines. Futher, we maintain a variable \text{maxarea}maxarea to store the maximum area obtained till now. At every step, we find out the area formed between them, update \text{maxarea}maxarea and move the pointer pointing to the shorter line towards the other end by one step.

The algorithm can be better understood by looking at the example below:

1 8 6 2 5 4 8 3 7
'''
def maxArea(height):
    
    water = 0
    head = 0
    tail = len(height) - 1

    for cnt in range(len(height)):
        
        width = abs(head - tail)
        
        if height[head] < height[tail]:   
            res = width * height[head]
            head += 1
        else:
            res = width * height[tail]
            tail -= 1

        if res > water:
            water = res

    return water



    
height = [1,8,6,2,5,4,8,3,7]
height = [1,2,1]
height = [1,1]
print(maxArea(height))