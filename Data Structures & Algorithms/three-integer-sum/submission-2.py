class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            tuples = self.findTwoSum(nums, i + 1, -nums[i])
            for tup in tuples:
                res.append([nums[i], tup[0], tup[1]])
        
        return res
    
    def findTwoSum(self, nums, start, target):
        l, r = start, len(nums) - 1
        tuples = []
        while l < r:
            small, large = nums[l], nums[r]
            if small + large == target:
                tuples.append([small, large])
                while l < r and nums[l] == small:
                    l += 1
                while l < r and nums[r] == large:
                    r -= 1
            elif small + large < target:
                l += 1
            elif small + large > target:
                r -= 1
        
        return tuples