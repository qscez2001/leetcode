'''
Implement pow(x, n), which calculates x raised to the power n (i.e. xn).

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

'''
# run time error
def myPow(x, n):
    print(n)
    if n < 0:
        return 1/myPow(x, -n)
    elif n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return x*myPow(x, n-1)


# others solution using helper (not quite understand

def myPow(x: float, n: int) -> float:
    if n >= 0:
        return helper(x, n) #1
    else:
        return 1/helper(x, -n) #2


# Second part
    
def helper(x, n): 
    if n == 0: #3
        return 1
    
    temp = myPow(x, n//2) #4
    # print(temp)
    if n % 2 == 0: #5
        return  temp * temp
    else:
        return temp * temp * x #6

x = 2.00000
n = 10
print(myPow(x, n))
x = 2.10000
n = 3
print(myPow(x, n))
x = 2.00000
n = -2
print(myPow(x, n))
x = 0.00001
n = 2147483647
print(myPow(x, n))