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
        if head is None:
            return None
        
        nodes = [head]
        current_node = head
        while current_node.next is not None:
            next_node = current_node.next
            nodes.append(next_node)
            current_node = next_node

        sz = len(nodes)
        # print('sz', sz)
        # print(nodes)

        i = sz - n

        if sz == 1:
            return None
        
        if i == 0:
            return nodes[1]
        elif n == 1:
            nodes[-2].next = None
            return head
        else:
            nodes[i - 1].next = nodes[i + 1]
            return head
        # pass

if __name__ == '__main__':
    # print(build_linked_list([1,2,3]))
    sol = Solution()
    print(sol.removeNthFromEnd(
        build_linked_list([1,2,3,4,5]),
        2)) # [1,2,3,5]
    # print(sol.removeNthFromEnd([1], 1)) # []
    # print(sol.removeNthFromEnd([1,2], 1)) # [1]
