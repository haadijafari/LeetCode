# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        return self.dummy(1,n)

    def dummy(self, start, end) -> int:
        mid = int((end+start) / 2)
        if isBadVersion(mid - 1) == False and isBadVersion(mid) == True:
            return mid
        
        if isBadVersion(mid) == True:
            return self.dummy(start, mid-1)
        else:
            return self.dummy(mid+1, end)
