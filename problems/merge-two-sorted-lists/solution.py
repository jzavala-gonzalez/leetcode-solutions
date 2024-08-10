# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        current1 = list1
        current2 = list2
        
        head = None
        trailing = None
        while current1 or current2:
            other_is_none = False
            
            if current1 is None:
                other_is_none = True
                chosen_node = current2
                current2 = current2.next
            elif current2 is None:
                other_is_none = True
                chosen_node = current1
                current1 = current1.next
            elif (current1.val <= current2.val):
                chosen_node = current1
                current1 = current1.next
            else:
                chosen_node = current2
                current2 = current2.next
                
            if not trailing:
                head = chosen_node
                trailing = head
            else:
                trailing.next = chosen_node
                trailing = chosen_node
                
            if other_is_none:
                break
                
        return head