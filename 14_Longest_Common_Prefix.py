def longestCommonPrefix(strs):
    
    if not strs:
        return ""

    length = []
    for str in strs:
        length.append(len(str))
    min_len = min(length)

    if len(strs) == 1:
        return strs[0]
    
    flag = 1
    output = ""
    for j in range(min_len):
        num = 0
        for i in range(len(strs)-1):
            # print(strs[i][j], strs[i+1][j])
            if strs[i][j] == strs[i+1][j] and flag:
                num += 1
            else:
                flag = 0
        if num == len(strs)-1:
            output = output + strs[i][j]
        # print(num)

    return output

# others solution
def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs: return ""
    if len(strs) == 1: return strs[0]
    
    strs.sort()
    p = ""
    for x, y in zip(strs[0], strs[-1]):
        if x == y: p+=x
        else: break
    return r

# def longestCommonPrefix(strs):
#     if (len(strs) == 0): return ""
#     prefix = strs[0]
#     for i in range(1, len(strs)):
#         while (strs[i].find(prefix) != -1):
#             prefix = prefix
#             if (prefix.isEmpty()): return ""
    
#     return prefix


input = ["flower","flow","flight"]
input = ["dog","racecar","car"]
input = ["aca","cba"]
print(longestCommonPrefix(input))