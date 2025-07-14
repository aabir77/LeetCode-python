from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:  # base case: if array is empty
            return None

        mid = len(nums) // 2  # middle index
        root = TreeNode(nums[mid])  # create node from middle

        # Recursively build left and right subtrees
        root.left = self.sortedArrayToBST(nums[:mid])       # left half
        root.right = self.sortedArrayToBST(nums[mid+1:])    # right half

        return root