class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        for i in range(1, len(prefix)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        for i in range(len(postfix) - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]
        
        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * postfix[i])
        return res