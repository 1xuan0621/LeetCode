import collections
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        l1, l2 = [0] * 26, [0] * 26

        for i in range(len(s1)):
            l1[ord(s1[i]) - ord('a')] += 1
            l2[ord(s2[i]) - ord('a')] += 1
        
        match = 0
        for i in range(26):
            match += (1 if l1[i] == l2[i] else 0)
        l = 0
        for r in range(len(s1), len(s2)):
            if match == 26: return True
            print(match)
            index = ord(s2[r]) - ord('a')
            l2[index] += 1
            if l1[index] == l2[index]:
                match += 1
            elif l1[index] + 1 == l2[index]:
                match -= 1

            index = ord(s2[l]) - ord('a')
            l2[index] -= 1
            if l1[index] == l2[index]:
                match += 1
            elif l1[index] - 1 == l2[index]:
                match -= 1
            l += 1
        print(l1,l2)
        return match == 26
s1 = 'abc'
s2 = 'bbbca'

print(Solution().checkInclusion(s1, s2))