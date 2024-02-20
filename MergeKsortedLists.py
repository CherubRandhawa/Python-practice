class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            kMergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                kMergedLists.append(self.mergeList(l1, l2))
            lists = kMergedLists #after processing all the pairs putting k mergedlists into lists
        
        return lists[0]
    
    def mergeList(self, l1, l2):
        dummy = ListNode()       #DUMMY IS START OF LINKED LIST WIYH NO NODE, TAIL IS UDES TO KEEP TRAKC OF LAST NODE BY TAIL.NEXT
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            
            else:
                tail.next = l2
                l2 = l2.next
            
            tail = tail.next
        
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        
        return dummy.next      #DUMMY.NEXT RETURNS THE FIRDT ELEMENT OF LINKED LIST
