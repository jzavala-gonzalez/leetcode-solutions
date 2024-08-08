from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f'ListNode(val={self.val}, next={self.next})'

def build_linked_list(list_values):
    n = len(list_values)
    if n == 0:
        return None
    
    return ListNode(val=list_values[0],
                    next=build_linked_list(list_values[1:])
                    )
    

    

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # print('head', head)
        slow = head
        fast = head

        for _ in range(n):
            fast = fast.next

        if fast is None:
            return head.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head

if __name__ == '__main__':
    # print(build_linked_list([1,2,3]))
    sol = Solution()
    print(sol.removeNthFromEnd(
        build_linked_list([1,2,3,4,5]),
        2)) # [1,2,3,5]
    # print(sol.removeNthFromEnd([1], 1)) # []
    # print(sol.removeNthFromEnd([1,2], 1)) # [1]
