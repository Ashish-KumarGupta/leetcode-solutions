# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        last = None
        curr = head
        while curr:
            temp = curr.next
            # curr.next = last
            # last = curr
            curr.next, last = last, curr
            curr = temp
        return last