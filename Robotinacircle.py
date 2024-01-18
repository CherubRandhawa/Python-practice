#LEETCODE 1041 ROBOT BOUND IN A CIRCLE

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
         # if the rotot returns at the origin then its true
    # or if the robot changes direction i.e 
    #the final direction is not north then true
        direction=0 # current direction ,possible dir-> N=0, W=1, S=2, E=3
        x,y=0,0 #X and y co-ordinate
        for ins in instructions:
            if ins == "G":
                if direction == 0: #N
                    y+=1
                elif direction == 1:#W
                    x-=1
                elif direction == 2:#S
                    y-=1
                elif direction == 3:#E
                    x+=1
            elif ins=="L":
                direction=(direction+1)%4 #mod by 4 so direction can have values
            elif ins=="R":                # as (0,1,2,3) only as they are the 
                direction=(direction-1)%4 # defined directions
            
        if x == 0 and y == 0:
            return True
        elif direction!=0:
            return True
        else:
            return False