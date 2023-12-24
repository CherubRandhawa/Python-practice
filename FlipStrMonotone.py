def minFlipsMonoIncr(self, s: str) -> int:
        countone = 0 #to keep track on one and not 0 coz 1 is on right and we are traversing to right, so we can change 1 anytime but not zero
        res = 0 # to keep track of minimum flips 
        for i in range(len(s)): 
            if s[i] == '1':
                countone += 1
            else:
                res = min(res+1, countone) #whenever there i 0 or array i finished; it compares min of res+1 where 1 is for last element
        return res
#Compared with countone to see if number of flips of 1 are less as compared to those of 0