"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

--------------------
Constraints
The number of nodes in the list is in the range [1, 5 * 10^4].
1 <= Node.val <= 1000
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def cutinhalf(head):
    fast, slow = head.next, head

    if not fast:
        return None

    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

    if fast.next:
        slow = slow.next
    k = slow.next
    slow.next = None

    return k


def reverse(head):
    if not head or not head.next:
        return head
    p, c, n = head, head.next, head.next.next

    p.next = None

    while n:
        c.next = p
        p, c, n = c, n, n.next

    c.next = p
    return c


def reorderList(head):
    """
    Do not return anything, modify head in-place instead.
    """
    h = cutinhalf(head)
    h = reverse(h)

    p = head
    while p and h:
        h2 = h.next
        h.next = p.next
        p.next = h

        p = p.next.next
        h = h2


head = [1, 2, 3, 4]
# head = [1,2,3,4,5]