# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from tkinter.messagebox import NO
from typing import List, Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        if not l1 and not l2:
            return None
        l3 = ListNode()
        p = l3
        pre = 0
        while p1 and p2:
            node = ListNode(p1.val+p2.val+pre)
            if node.val >= 10:
                pre = 1
                node.val -= 10
            else:
                pre = 0
            p.next = node
            p = p.next
            p1 = p1.next
            p2 = p2.next

        left = p1 if p1 else p2
        
        while left:
            node = ListNode(left.val+pre)
            if node.val >= 10:
                pre = 1
                node.val -= 10
            else:
                pre = 0
            p.next = node
            p = p.next
            left = left.next

        if pre > 0:
            node = ListNode(pre)
            p.next = node
        
        return l3.next
