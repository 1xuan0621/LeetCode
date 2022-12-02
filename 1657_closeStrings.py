class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): return False

        count1 = {}
        count2 = {}

        for i in range(len(word1)):
            count1[word1[i]] = 1 + count1.get(word1[i], 0)
            count2[word2[i]] = 1 + count2.get(word2[i], 0)
        
        if set(count1.keys()) == set(count2.keys()):
            return sorted(count1.values()) == sorted(count2.values())
        
        return False


word1 = 'uau'
word2 = "ssx"
print(Solution().closeStrings(word1, word2))