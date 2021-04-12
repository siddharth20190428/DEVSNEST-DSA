"""
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

----------------
Constraints
The number of nodes in the linked list is in the range [0, 10^4].
-10^6 <= Node.val <= 10^6

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def oddEvenList(head):
    if not head:
        return head
    odd, even = head, head.next

    even_head = even
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next

    odd.next = even_head
    return head


head = [1, 2, 3, 4, 5]
head = [2, 1, 3, 5, 6, 4, 7]
