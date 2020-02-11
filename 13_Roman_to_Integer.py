

def romanToInt(s):
    values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    romans = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
    integer = 0
    i = 0

    while i < len(s)-1:
        j = i+1
        if s[i]+s[j] in romans:
            integer = integer + values[romans.index(s[i]+s[j])]
            i += 2
        else:
            integer = integer + values[romans.index(s[i])]
            i += 1
            
    if i == len(s) - 1:
        integer = integer + values[romans.index(s[i])]

    return integer

# others solution... faster
def romanToInt(self, s):
    roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    z = 0
    for i in range(0, len(s) - 1):
        if roman[s[i]] < roman[s[i+1]]:
            z -= roman[s[i]]
        else:
            z += roman[s[i]]
    return z + roman[s[-1]]

# print(romanToInt("LVIII"))
# print(romanToInt("MCMXCIV"))
print(romanToInt("MDCXCV"))