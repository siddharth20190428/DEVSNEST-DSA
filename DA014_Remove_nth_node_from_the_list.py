"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?

-------------------
Constraints

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):
    if not head.next:
        return None
    one, two = head, head

    for _ in range(n):
        two = two.next

    if not two:
        head = one.next
        return head

    while two.next:
        one = one.next
        two = two.next

    one.next = one.next.next

    return head


head = [1, 2, 3, 4, 5]
n = 2
# head = [1]
# n = 1
# head = [1,2]
# n = 1