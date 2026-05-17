class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_idx = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_to_idx:
                return [num_to_idx[complement], i]
            num_to_idx[nums[i]] = i
        return []