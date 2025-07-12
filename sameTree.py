# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution :
  def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode])-> bool:
    if not p and not q :    #both nodes are none
       return True  # if both has no value means they are structurally same
    
    if not p or not q:
       return False  # if either of them is empty then return false
    
    if p.val != q.val :   #if both trees present and then checking their values
       return False  # if their value is not same then it will return false otherwise it will return true
    return self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right) # if the left and right nodes of both trees are same athen return it
# for checking both tree in VS code
p = TreeNode(1)  # root node
p.left = TreeNode(2)
p.right = TreeNode(3)  

q = TreeNode(1)  # root node
q.left = TreeNode(2)
q.right = TreeNode(3)

sol = Solution()
result = sol.isSameTree(p , q)
print("Are the trees are the same?",result)

