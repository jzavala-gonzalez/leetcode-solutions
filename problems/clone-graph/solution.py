"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        new_nodes_map = dict()

        def cloneNode(old_node):
            val = old_node.val
            if val in new_nodes_map:
                return new_nodes_map[val]
            
            new_node = Node(val = val, neighbors = [])
            new_nodes_map[val] = new_node

            for n in old_node.neighbors:
                new_node.neighbors.append(cloneNode(n))
            # neighbors = [cloneNode(n) for n in old_node.neighbors]
            # new_node.neighbors = neighbors

            return new_node

        return cloneNode(node) if node is not None else None
        