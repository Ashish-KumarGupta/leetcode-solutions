# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        # curr = head
        # if(not head):
        #     return
        # while curr.next:
        #     if curr.next.val == val:
        #         curr.next = curr.next.next
        #     else:
        #         curr = curr.next
        # if head.val == val:
        #     head = head.next
        # return head

        if head == None:
            return None
        nextNode = self.removeElements(head.next, val)
        if head.val == val:
            return nextNode
        head.next = nextNode
        return head