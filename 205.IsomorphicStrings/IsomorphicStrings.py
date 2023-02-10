class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def numberize(s: str()):
            looked , dic = [] , {}
            i = 1
            for ch in s:
                if ch not in dic:
                    dic[ch] = i
                    i+=1
                looked.append(dic[ch])
            return looked
        return numberize(s) == numberize(t)
    
# print(Solution.isIsomorphic(Solution, s ='egg', t ='add'))