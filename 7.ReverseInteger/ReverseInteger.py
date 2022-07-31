class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        if x < 0:
            negative = True
            x *= -1
        rev = 0
        while x >= 1:
            rev *= 10
            rev += (x % 10)
            x = x // 10
        
        if negative == True:
            rev *= -1
        
        if (rev > (-(2**31))) and (rev < (2**31)):
            return rev
        else:
            return 0
        