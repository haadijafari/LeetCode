class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openANDclose = {'}': '{', ']': '[', ')': '('}
        for i in s:
            if i in openANDclose:
                if stack and stack[-1] == openANDclose[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return True if not stack else False

## Testing the program
# s = Solution()
# print(s.isValid(""))
