#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#


# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        sl = list(s)
        for i in range(len(sl)):
            if sl[i] in dic.keys():
                dic[sl[i]][1] += 1
            else:
                dic[sl[i]] = [i, 1]
        for key in dic.keys():
            if dic[key][1] == 1:
                return dic[key][0]
        return -1


# @lc code=end
