# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        t1 = l1
        t2 = l2
        carry = 0
        dummyNode = ListNode(-1)
        curr = dummyNode

        while t1 != None or t2 != None:
            sm = carry

            if t1:
                sm += t1.val
                t1 = t1.next

            if t2:
                sm += t2.val
                t2 = t2.next

            newNode = ListNode(sm % 10)
            carry = sm // 10

            curr.next = newNode
            curr = curr.next

        if carry:
            curr.next = ListNode(carry)

        return dummyNode.next