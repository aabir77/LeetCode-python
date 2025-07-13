from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
  def isSymmetric(self, root: Optional[TreeNode])-> bool:
    def isMirror(left, right):
      if not left and not right:  # if both node empty neturn true
        return True 
      
      if not left or not right:  # or compare if one of them is empty
        return False
      if left.val != right.val:  # if value is not equal then return false
        return False
      # chcecking left and right is node is mirror of itself 
      return isMirror(left.left, right.right) and isMirror(left.right, right.left)
    return isMirror(root.left, root.right) if root else True 
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(3), TreeNode(4))
root.right = TreeNode(2,TreeNode(4), TreeNode(3))
sol = Solution()
print("is Symmetric?", sol.isSymmetric(root))