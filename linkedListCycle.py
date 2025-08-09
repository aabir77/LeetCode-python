from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
  def hasCycle(self, head: Optional[ListNode]) -> bool:
    slow = head # slow start at head 
    fast = head # fast also start at head
    while fast and fast.next: # while fast runner can keep going, so we will go untill it comes up with a circle
        slow = slow.next #slow moves one step at a time
        fast = fast.next.next # fast moves two steps at a time

        if slow == fast:  # if fast runs and came back to slow again, then there is a circle
          return True # if they meet, loop found
    return False #fast reached the end -> no loop
  
