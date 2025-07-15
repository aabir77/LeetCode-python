from typing import Optional


class TreeNode:
  def __init__(self, val=0, left=None, right = None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
  def isBalanced(self, root:Optional[TreeNode])->bool:   # this will give us a bool value only, but we also need height to solve the problem
    def check(node): #height of the subtree,  subtree is balanced or not.
      if not node:
        return 0 # height of an empty tree is 0
      # checking if the left and right subtree is balanced or not
      left = check(node.left) # calling node fn and said check your left subtree
      if left == -1: # if left subtree is unbalanced 
        return -1 # return its unbalanced..   -1 is a sign theat means unbalanced
      right = check(node.right) 
      if right == -1:
        return -1
       #after getting height  If the height difference is more than 1, we return -1 — meaning "not balanced".
      if abs(left - right) > 1 :
        return -1  # current node is unbalanced 
      return 1 + max(left,right)  # return height of current node's subtree
    
    return check(root) != -1  # balanced if check did not return -1
      
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

sol = Solution()
print(sol.isBalanced(root))  

