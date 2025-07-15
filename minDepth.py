
from typing import Optional

class TreeNode:
  def __init__(self, val = 0, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
  def minDepth(self, root: Optional[TreeNode])-> int:
    if not root :
      return 0 # if tree is none, depth is 0
    
    # if left is none, go right
    if not root.left:
      return 1 +  self.minDepth(root.right)
    
    # if right is none, go left
    if not root.right:
      return 1 + self.minDepth(root.left)
    
     # Both children exist: return minimum of both sides
    return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
  
   # VS CODE print
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sol = Solution()
print(sol.minDepth(root))
