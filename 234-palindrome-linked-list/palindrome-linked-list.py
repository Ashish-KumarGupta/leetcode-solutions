# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if(head == None or head.next == None):
            return True
        
        mid = self.findMid(head)


        prev = None
        curr = mid
        while(curr):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        right = prev
        left = head

        while(right != None):
            if (left.val != right.val):
                return False
            left = left.next
            right = right.next
        return True
    
    def findMid(self, head):
        slow = head
        fast = head
        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
        return slow