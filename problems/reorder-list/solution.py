# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slow = head
        fast = head.next # 1 ahead so we get slow one node back

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow is now the last node in the normal-direction half of the list
        second = slow.next # start of second half of list
        slow.next = None # CUT the list into two pieces

        # Reverse the second half of the list
        prev = None # previous in normal direction / next in reversed direction
        while second:
            next_second = second.next # cache before editing

            second.next = prev # Reversal: Point node to previous node

            # Prepare for next iteration
            prev = second
            second = next_second
        # The head of the reversed list is now stored in prev
        # (because second had to become the trailing None to exit the loop)

        # Join both lists
        first, second = head, prev # head of normal direction, head of reversed dir
        while second:
            # cache
            next_first = first.next
            next_second = second.next

            # Chain together
            first.next = second
            second.next = next_first

            # Prepare for next iteration
            first = next_first
            second = next_second
        # breaks after we run out of second nodes
        # should there be an extra normal-direction node,
        # it is added to the chain at second.next, as next_first
        # (or final_first, I guess)