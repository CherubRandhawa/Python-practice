class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
	
	# TAKING SLOW TO MIDDLE AND FAST TO NEXT
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        #REVERSING THE HLAF OF LINKED LIST
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        #CHECKING IF PALINDROME
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            
            left = left.next
            right = right.next
        
        return True
