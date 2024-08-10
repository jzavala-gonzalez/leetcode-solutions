# Esta solucion me encanta cuan sencilla y corta es,
# mantiene legibilidad, pero aparentemente toma un chin más
# tiempo que la primera.
# La primera tomó 41ms y esta 44ms pero los pros
# de esta solución vencen su leve retraso.

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
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