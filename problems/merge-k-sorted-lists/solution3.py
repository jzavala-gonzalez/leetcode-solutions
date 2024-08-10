# Best one yet! 65ms, beats 96.98% of solutions
# Definition for singly-linked list.
import heapq
from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        # Use heap to always pick smallest-valued node
        i = 0
        heap = []
        for head in lists:
            if head:
                heapq.heappush(heap, (head.val, i, head)) # val for sorting, head for reference
                i += 1
        
        # Get the "sorted" nodes back
        # (it's just a queue i guess)
        dummy = ListNode(0)
        current_node = dummy
        while heap:
            current_node.next = heapq.heappop(heap)[2]
            current_node = current_node.next
            if current_node.next:
                heapq.heappush(heap, (current_node.next.val, i, current_node.next))
                i += 1

        return dummy.next