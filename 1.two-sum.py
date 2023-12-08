#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        for i in range(l):
            for j in range(l):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]
        return []


# @lc code=end
