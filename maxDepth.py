# Definition for a binary tree node.
from typing import Optional


class TreeNode:
 def __init__(self, val=0, left = None, right = None) :
  self.val = val
  self.left = left
  self.right = right
class Solution :
 def maxDepth(self, root: Optional[TreeNode])-> int:
   if root is None:
    return 0  #base case 
   left_depth = self.maxDepth(root.left) # telling self, inside you thers a maxDepth fn, from there go to left from the root by(root.left)
   right_depth = self.maxDepth(root.right)# telling self, inside you thers a maxDepth fn, from there go to right from the root by(root.right)

   return 1 + max(left_depth, right_depth)  # taking max of left and right node and adding 1 because we are starting from root node
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sol = Solution()
depth = sol.maxDepth(root)
print("Maximum Depth:", depth)