#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = ""
        while l1:
            s1 = str(l1.val) + s1[:]
            l1 = l1.next
            
        s2 = ""
        while l2:
            s2 = str(l2.val) + s2[:]
            l2 = l2.next
            
        x = str(int(s1) + int(s2))
        l = None
        for y in x:
            l = ListNode(int(y),l)
        
        return l
        
        
# @lc code=end

