class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freqDic = {}
        for char in s:
            freqDic[char] = freqDic.get(char, 0) + 1
        for char in t:
            if char not in freqDic:
                return False
            if char in freqDic:
                freqDic[char] -= 1
            if freqDic[char] < 0:
                return False
        return True

                
        