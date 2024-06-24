from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        p1 = head
        p2 = p1.next
        p3 = p2.next

        while p3:
            p2.next = p1

            p1 = p2
            p2 = p3
            p3 = p2.next
        p2.next = p1

        head.next = None
        return p2


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    p2 = Solution().reverseList(head)

    print()