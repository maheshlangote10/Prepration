# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 1
        while head.next != None:
            count += 1
            head = head.next
        print(count)


node3 = ListNode(3)
node2= ListNode(2, node3)
node1 = ListNode(1, node2)

obj = Solution()
obj.middleNode(node1)

