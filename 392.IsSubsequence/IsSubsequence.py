class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '':
            return True
        for i in range(len(s)):
            if s[i] not in t:
                return False
            t = t[t.find(s[i])+1:]
        return True
    
# print(Solution.isSubsequence(Solution, "axc", "ahbgdc"))