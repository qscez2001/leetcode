# 寫了一堆if, else, 很多重複

# others solution
def intToRoman(num: int):
    
    values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
    res = ""
    for i, v in enumerate(values):
        print(res)
        res += (num//v) * numerals[i]
        print(num)
        num %= v
    return res

print(intToRoman(1994))
    
