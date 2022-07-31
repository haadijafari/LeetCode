class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        def pal_check (s):
            return (s == s[::-1])
        
        
        biggest_pal = s[0]
        r = len(biggest_pal) // 2
        
        # one centered:
        for center in range(1, len(s)-1):
            wide = [(center - r -1), (center + r + 1)]
            while (wide[0] > -1 and wide[1] < len(s)):
                if pal_check(s[wide[0]:wide[1]+1]):
                    biggest_pal = s[wide[0]:wide[1]+1]
                    r = len(biggest_pal) // 2
                    wide[0] -= 1
                    wide[1] += 1
                else:
                    break
                    
        # two centered:
        for center in range(r, len(s)-r-1):
            wide = [(center - r), (center + r + 1)]
            while (wide[0] > -1 and wide[1] < len(s)):
                if pal_check(s[wide[0]:wide[1]+1]):
                    biggest_pal = s[wide[0]:wide[1]+1]
                    r = len(biggest_pal) // 2
                    wide[0] -= 1
                    wide[1] += 1
                else:
                    break
        
        
        return (biggest_pal)