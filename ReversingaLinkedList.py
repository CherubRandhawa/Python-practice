class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr is not None:
            nxt = curr.next        #storing next node in a variable
            curr.next = prev       #now next node will be the previous one i.e none in case of first node
            prev = curr            #prev node will store the curr node now i.e moving forward in linked list
            curr = nxt             # the next node we stored will becomw the current node
        
        return prev