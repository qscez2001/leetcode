def lengthOfLongestSubstring(self, s: str) -> int:
    maxlen = 0
    for i in range(len(s)):
        temp = []
        temp.append(s[i])
        for j in range(i+1, len(s)):
            if s[j] not in temp:
                temp.append(s[j])
            else:
                break
        if len(temp) > maxlen:
            maxlen = len(temp)
    return maxlen
