#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or not k:
            return head

        n = 1
        # count O(n)
        node = head
        while node.next:
            n += 1
            node = node.next
        # connect last to head (circular list)
        node.next = head

        # transverse to node before the new head
        r = k % n
        node = head
        for _ in range(n - r - 1):
            node = node.next

        ans = node.next
        node.next = None

        return ans


# @lc code=end
