#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#


# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:  # [5,4,-1,7,8]
        MAX = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i - 1] + nums[i])
            MAX = max(MAX, nums[i])
        return MAX


# @lc code=end
