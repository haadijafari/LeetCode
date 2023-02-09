class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right = sum(nums)
        left = 0
        
        for i in range(len(nums)):
            right -= nums [i]
            if left == right:
                return i
            left += nums[i]
        return -1