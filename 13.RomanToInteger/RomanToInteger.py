class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        the_number = 0
        dic_valu = {"IV":4, "IX":9, "XL":40, "XC":90, "CD":400,
                    "CM":900, "I":1, "V":5, "X":10, "L":50, "C":100,
                    "D":500, "M":1000}
        
        num_list = ["IV", "IX", "XL", "XC", "CD", "CM", "I",
                    "V", "X", "L", "C", "D", "M"]
        
        for number in num_list:
            if (s.find(number)+1):
                the_number += s.count(number) * dic_valu[number]
                s = s[:s.find(number)] + s[s.find(number)+2:]
        
        return the_number