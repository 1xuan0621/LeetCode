def strStr(haystack: str, needle: str):
    if needle not in haystack:return -1
    if not needle: return 0
    a = len(haystack)
    for i in range(a):
        if haystack[i:i+len(needle)] == needle:
            return i

print(strStr(haystack = "aaaaa", needle = "bba"))