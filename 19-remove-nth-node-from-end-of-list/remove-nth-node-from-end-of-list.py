# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        size = 0
        curr = head
        while curr != None:
            curr = curr.next
            size +=1

        if(n == size):
            head = head.next
            return head

        i = 1
        iToFind = size - n
        prev = head
        while(i < iToFind):
            prev = prev.next
            i += 1
        
        prev.next = prev.next.next
        return head