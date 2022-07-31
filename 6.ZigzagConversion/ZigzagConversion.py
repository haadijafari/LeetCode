class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        if numRows == 1:
            return s
        else:
            my_list = []
            for i in range(numRows):
                my_list.append('')

            while True:
                for i in range(numRows):
                    my_list[i] = my_list[i] + s[0]
                    if len(s) == 1:
                        return(''.join(my_list))
                    s = s[1:]

                for i in range(numRows-2, 0, -1):
                    my_list[i] = my_list[i] + s[0]
                    if len(s) == 1:
                        return(''.join(my_list))
                    s = s[1:]