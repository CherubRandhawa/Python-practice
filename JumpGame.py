class Solution:
    def canJump(self, nums: List[int]) -> bool:
      jumps = 0 #initial number of jumps we hhave

      for n in nums:
          if jumps < 0:                 #WE HAVE NO MORE JUMPS LEFT
              return False            
          elif n > jumps:              #IF CURRENT NUMBERS IS BIGGER THAN CURRENT JUMPS WE HAVE PICK IT UP AND INCREASE THE JUMPS TP THAT NUMBER
              jumps = n
          jumps -=1                      #REDUCE 1 JUMP AFTER VERY ITERATION

      return True
