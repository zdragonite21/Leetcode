#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p, p.next = self, head
        while p.next and p.next.next:
            a = p.next
            b = a.next
            p.next, b.next, a.next = b, a, b.next
            p = a
        return self.next


# @lc code=end
