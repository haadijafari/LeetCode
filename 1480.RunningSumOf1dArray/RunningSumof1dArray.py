class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = []
        sum = 0
        for i in nums:
            sum += i
            answer.append(sum)
        return answer