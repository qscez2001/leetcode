# n-choose-k
# recursive, factorial, and multiplicative

def nck_recursive(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return nck_recursive(n-1, k) + nck_recursive(n-1, k-1)

def fact(n):
    if n <= 1:
        return 1
    else:
        return n*fact(n-1)
# n! / (k! * (n- k)!)
def nck_factorial(n, k):
    return fact(n) / (fact(k) * fact(n-k))

def nck_multiplicative(n, k):
    result = 1
    for i in range(1, k+1):
        result = result * (n-(k-i))/i
    return result


