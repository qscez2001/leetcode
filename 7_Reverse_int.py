# my solution
def reverse(self, x: int) -> int:
    stri = ""
    negative = False
    if x < 0:
        negative = True
        stri = str(x)[1:]
    else:
        stri = str(x)
            
    new = ""
    for i in stri:
        new = i + new
        
    if int(new) > pow(2, 31) - 1:
        return 0
        
    if negative:
        new = "-" + new
            
    return int(new)