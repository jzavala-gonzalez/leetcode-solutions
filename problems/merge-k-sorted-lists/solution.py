# Very slow, only faster than 8% of solutions lol
# 2294ms, beats 8.78%

# Definition for singly-linked list.
from typing import Optional, List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        big_list = None
        while lists:
            l = lists.pop()
            big_list = self.mergeTwoLists(big_list, l)
        return big_list
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # If both are none, still returns none (e.g. list2).
        # Otherwise returns the non-null one
        # This is a great pattern I should remember
        if not list1 or not list2:
            return list1 if list1 else list2

        # By now both lists are non-null, they have values
        # Use the "list1" variable as a proxy for the lower-valued list...
        if list1.val > list2.val:
            list1, list2 = list2, list1

        # ...so we always append to "list1" and we don't worry about
        # the arbitrary variable name we've defined.
        # No need to be strict about maintaining the naming
        list1.next = self.mergeTwoLists(list1.next, list2)
        return list1 # Return the head of the lower-valued list