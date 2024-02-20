class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # Skip positive integers
            if a > 0:                #AS ARRAY IS SRTED SUM INVOLVING A POSV INTEGER EITH 2 OTHER ELEMENTS WOULD BE > 0
                break

            if i > 0 and a == nums[i - 1]:   #COMAPRE CURRENT ELEMENT TO PREVIOUS ELEMENT AND IF THEY ARE SAME, SKIP THE ITERATION TO AVOID DUPLICACY 
                continue

            l, r = i + 1, len(nums) - 1     #2 POINTERS L AND R AND TOTAL SUMM IF  == 0 APPEND IN ARRAY 
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r: #STILL CHECKING HERE FOR DUPLICATES COMPARING L WITH L - 1 AND MOVE  L+= 1
                        l += 1
                        
        return res
