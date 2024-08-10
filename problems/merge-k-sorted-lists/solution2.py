# Fast AF to just sort. 70ms, beats 89.11% of solutions
# Shouldn't this be the "inefficient" solution?

# Definition for singly-linked list.
from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        all_values = []
        nlists = len(lists)
        for i in range(nlists):
            node = lists[i]
            while node:
                all_values.append(node.val)
                node = node.next
        all_values.sort()

        head_none = ListNode(val=None)
        node = head_none
        for v in all_values:
            new_node = ListNode(val=v)
            node.next = new_node
            node = new_node
        return head_none.next