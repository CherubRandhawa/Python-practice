ARR = [100, 4, 200, 1, 3, 2]

def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)  #CHANGED NUMS TO NUMSET SO NO DUPES
        longest = 0         # LONGEST SET -> 0

        for n in nums:
            #checking for start of a sequence
            if (n - 1) not in numSet:         #THIS WILL UNIQUELY BRING US TO THE SMALLEST ELEMENT OF THE SEQ
                length = 0                    #LENGHT = 0 SET AT EVERY ITERATION
                #checking for successor
                while (n + length) in numSet: # CHECKIN FOR SUCCESOR IF THERE 
                    length += 1		      # IF FOUND IN NUMSET INCREASE LENGTH AND AGAIN CGHECK USING WHILE LOOP
                longest = max(length, longest) # IN LONGEST STORE MAXIMUM OF LENGTH AND LONGEST
        return longest

