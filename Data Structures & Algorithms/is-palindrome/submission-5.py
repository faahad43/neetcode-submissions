class Solution:
    def isPalindrome(self, s: str) -> bool:
        string =''.join(char for char in s if char.isalnum()).lower()
        length = len(string)

        l = 0
        r= length - 1
        idx=0
        while idx < length:
            if string[l] == string[r]:
                l +=1
                r -=1
                if l == r or r == l-1:
                    return True
                else:
                    idx +=1
                    continue
            else:
                return False
        return True