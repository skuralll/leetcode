#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#


# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lefts = ["(", "{", "["]
        rights = [")", "}", "]"]
        for c in list(s):
            if c in lefts:
                stack.insert(0, c)
            else:
                if stack == [] or rights[lefts.index(stack.pop(0))] != c:
                    return False
        if stack != []:
            return False
        return True


# @lc code=end
