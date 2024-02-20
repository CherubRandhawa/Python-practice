class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Start both fast and slow pointer at the head 
        
        slow, fast = head, head

        #get fast pointer to be n nodes ahead so that when fast is at end slow is one node before node to be removed

        for i in range(n):
            fast = fast.next
        # if fast pointer reaches end before n then that means len(ll) < n so return head.next
        if fast is None:
            return head.next
        #Travers ll until fast pointer reaches end and slow pointer is one node before nth node
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        
        #Remove the nth node by updating the next pointer of the node before it

        slow.next = slow.next.next

        return head