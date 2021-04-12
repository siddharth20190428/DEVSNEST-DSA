"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

----------------
Constraints
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    if not head or not head.next:
        return head
    p, c, n = head, head.next, head.next.next

    p.next = None

    while n:
        c.next = p
        p, c, n = c, n, n.next

    c.next = p
    return c


head = [1, 2, 3, 4, 5]
head = [1, 2]
head = []