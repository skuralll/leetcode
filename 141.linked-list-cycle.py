#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        count = 0
        max = 100000
        curr = head
        while curr is not None:
            count += 1
            if count > max:
                return True
            curr = curr.next
        return False


# @lc code=end
