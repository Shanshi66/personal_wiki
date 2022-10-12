# Definition for singly-linked list.
from email.quoprimime import header_decode
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums = set(nums)
        if not head:
            return 0
        p = head
        cnt = 0
        flag = False
        while p:
            if p.val in nums:
                flag = True
            elif flag:
                cnt += 1
                flag = False
            p = p.next
        if flag: # 注意末端边界
            cnt += 1
        return cnt


if __name__ == '__main__':
    test = Solution()
            