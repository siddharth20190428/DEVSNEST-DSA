"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

----------------
Constraints
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    if not l1 or not l2:
        return l1 if not l2 else l2
    n1, n2, k1, k2 = 0, 0, l1, l2

    while k1 or k2:
        if k1:
            n1, k1 = n1 + 1, k1.next
        if k2:
            n2, k2 = n2 + 1, k2.next
    if n2 > n1:
        n1, n2, l1, l2 = n2, n1, l2, l1

    ans, ans_p, carry, carry_p = None, None, None, None
    carry_till_now, p, dig1, dig2 = False, n1, l1, l2 if n1 == n2 else ListNode(0)

    while p != 0:
        p, carr, summ = (
            p - 1,
            ListNode((dig1.val + dig2.val) // 10),
            ListNode((dig1.val + dig2.val) % 10),
        )
        carry_till_now = carry_till_now or carr.val != 0
        if ans_p:
            ans_p.next = summ
        else:
            ans = summ
        ans_p = summ
        if carry_till_now:
            if carry_p:
                carry_p.next = carr
            else:
                carry = carr
            carry_p = carr
        dig1 = dig1.next
        if p == n2:
            dig2 = l2
        else:
            dig2 = dig2.next if p < n2 else ListNode(0)
    if carry_till_now:
        carry_p.next = ListNode(0)
        return addTwoNumbers(ans, carry)
    return ans


l1 = [7, 2, 4, 3]
l2 = [5, 6, 4]
# l1 = [2,4,3]
# l2 = [5,6,4]
# l1 = [0]
# l2 = [0]