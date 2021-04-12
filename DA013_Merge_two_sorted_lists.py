"""
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

-------------------
Constraints
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1, l2):
    k = ListNode()
    ans = k

    while l1 and l2:
        if l2.val > l1.val:
            k.next = l1
            l1 = l1.next
            k = k.next
        else:
            k.next = l2
            l2 = l2.next
            k = k.next
    k.next = l1 or l2
    return ans.next


l1 = [1, 2, 4]
l2 = [1, 3, 4]
# l1 = []
# l2 = []
# l1 = []
# l2 = [0]
