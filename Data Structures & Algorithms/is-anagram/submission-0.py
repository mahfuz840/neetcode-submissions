class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charCountOfS = [0] * 26
        charCountOfT = [0] * 26
        if len(s) != len(t):
            return False
        
        for charS in s:
            i = ord(charS) - ord('a')
            charCountOfS[i] = charCountOfS[i] + 1
        
        for char in t:
            i = ord(char) - ord('a')
            charCountOfT[i] = charCountOfT[i] + 1
        
        for i in range(26):
            if charCountOfS[i] != charCountOfT[i]:
                return False
        
        return True
