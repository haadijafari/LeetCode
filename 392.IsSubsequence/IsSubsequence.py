class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for ch in s:
            if ch in t:
                t = t[t.find(ch)+1:]
                continue
            return False
        return True