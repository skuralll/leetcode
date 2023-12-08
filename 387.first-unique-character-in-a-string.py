#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#


# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for c in list(s):
            if c in count.keys():
                count[c] += 1
            else:
                count[c] = 1
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        return -1


# @lc code=end
