def isAnagram( s: str, t: str):
    return all(s.count(x) == t.count(x) for x in 'abcdefghijklmnopqrstuvwxzy')
    
print(isAnagram(s = "aacc", t = "ccac"))