class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, target, 0, len(nums)-1)

    def binarySearch(self, nums, target, start, end):
        if end < start:
            return -1
        mid = int((end+start) / 2)
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            return self.binarySearch(nums, target, mid+1, end)
        else:
            return self.binarySearch(nums, target, start, mid-1)
