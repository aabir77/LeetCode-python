
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

from typing import Optional

class Solution:
  def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
    result = []
    stack = []
    current = root  # pointer that pointing at root

    while current or stack:  # while current pointer and stack is not empty
      while current:  # while our current pointer is not empty means runs from top to bottom
        stack.append(current)  # add the nodes of current pointer to stack
        current = current.left  # and searching to left nodes

      current = stack.pop()  # when we reach the empty node of left we will pop it and add it to the result
      result.append(current.val)  # ✅ fixed: adding the node's value to result
      current = current.right  # it will check the right then go back to while loop, do same pop operation and add 

    return result  # after popping and adding show the result

