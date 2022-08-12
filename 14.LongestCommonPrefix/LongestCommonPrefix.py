class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ''
        
        for i in range(len(strs[0])):
            for s in strs:
                if i >= len(s) or strs[0][i] != s[i]:
                    return result
            result += strs[0][i]
        
        return result
    

## Testing the program
# s = Solution()
# print(s.longestCommonPrefix(["flower","flow","flight"]))