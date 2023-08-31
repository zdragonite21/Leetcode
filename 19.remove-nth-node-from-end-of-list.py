#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # i = 0
        # if n == 0:
        #     return head.next
        # root = head
        # while head:
        #     if i == n:
        #         p.next = head.next
        #     p = head
        #     head = head.next
        #     i += 1
        # return root

        # ls = []
        # while head:
        #     ls.append(head)
        #     head == head.next

        # ls[-n - 1].next = ls[-n + 1]

        # return ls[0]

        nn = 0
        root = head
        while head:
            print(head.val, end=" ")
            nn += 1
            head = head.next

        if nn == 1:
            return None
        print()
        nn -= n
        i = 0
        head = root
        p = None
        while head:
            print(head.val, end=" ")
            if i == nn:
                if not p:
                    return head.next
                p.next = head.next
                break
            p = head
            head = head.next
            i += 1

        return root

        # root = head
        # while head:
        #     head = head.next
        # head = root
        # while head:
        #     head = head.next

        # return root


# @lc code=end
