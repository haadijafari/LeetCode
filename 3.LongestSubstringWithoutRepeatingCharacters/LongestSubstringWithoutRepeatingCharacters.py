class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        i = 0
        s_large = ''
        s_ans = ''
        while (i < len(s)):
            if (s[i] not in s_large):
                s_large = s_large + s[i]
                i+=1
                if not(i < len(s)):
                    if len(s_ans) < len(s_large):
                        s_ans = s_large

            else:
                if len(s_ans) < len(s_large):
                    s_ans = s_large
                    s_large = s_large[s_large.find(s[i])+1:] + s[i]
                    i+=1
                else:
                    s_large = s_large[s_large.find(s[i])+1:] + s[i]
                    i+=1


        return len(s_ans)
