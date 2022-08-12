class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # a string to save confirmed prefix string
        result = ''
        
        #loop through every charecter of first string
        for i in range(len(strs[0])):
            #loop through every string in the list
            for s in strs:
                #checks if the index is out of range or not
                #then checks if the chareckter is the same or not
                if i >= len(s) or strs[0][i] != s[i]:
                    #returns the result if the statement is true
                    return result
            #adds the charecter if everything is fine
            result += strs[0][i]
            
        #returns the result if the charecters are all checked
        return result
    

## Testing the program
# s = Solution()
# print(s.longestCommonPrefix(["flower","flow","flight"]))