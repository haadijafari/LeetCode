class Solution:
    def isValid(self, s: str) -> bool:
        #open parantheses are going to be added to "stack"
        #if we cross closed ones the last opened one will be removed
        stack = []
        #a hash map to see which open parantheses are for which closed ones
        openANDclose = {'}': '{', ']': '[', ')': '('}
        # going through the given string using for
        for i in s:
            # the condition that "i" is in our hash map (it is a closed one)
            if i in openANDclose:
                # if the stack is not empty
                # and if the last char of stack matches with "i"
                if stack and stack[-1] == openANDclose[i]:
                    # we can remove the open one and move to next "i"
                    stack.pop()
                else:
                    return False
            # "i" is an opened parantheses so we are free to add it to stack
            else:
                stack.append(i)

        # at the end if the stack is empty it means that all the parantheses had...
        # had pairs and are closed in the currect order and we can return "True"
        # if it is not empty then we return "False"
        return True if not stack else False

## Testing the program
# s = Solution()
# print(s.isValid(""))
