class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answerdic = dict()
        for i in range(len(nums)):
            num = nums[i]
            answer = target - num
            if num in answerdic:
                return[answerdic[num], i]
            else:
                answerdic[answer] = i
        return[]