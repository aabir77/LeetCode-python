#creating listNode
from typing import Optional


class ListNode:
  def __init__(self, val=0, next = None):
    self.val = val     #value of the node 
    self.next = next   #pointer of the next node
    
class Solution:
  def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode] :
    current = head  # starting with the first value 
    while current and current.next :
      if current.val == current.next.val : #if first value is equal to next value
        current.next = current.next.next  # then ignore the next value by doing this line of code

      else:
        current = current.next  # no duplicate: move to the next node
    return head # head will give us the value 


    