
def longestCommonPrefix(strs):
    if not strs: return ""
    s1 = min(strs)
    s2 = max(strs)
    
    for i, c in enumerate(s1):
        if c != s2[i]:
            return s1[:i]
    return s1  

print(longestCommonPrefix(strs = ["dog","racecar","car"]))