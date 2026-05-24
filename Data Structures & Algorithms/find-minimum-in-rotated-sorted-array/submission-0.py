class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[-1]:
                l = mid + 1
            elif nums[mid] < nums[-1]:
                r = mid - 1
            elif nums[mid] == nums[-1]:
                return nums[-1]
        return nums[l]