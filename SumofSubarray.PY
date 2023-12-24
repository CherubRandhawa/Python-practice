#

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        sm=0
        n=len(nums)
        for i in range(n-1):
            mx=nums[i]
            mn=nums[i]
            for j in range(i+1,n):
                
                mx=max(mx,nums[j])
                mn=min(mn,nums[j])
                sm+=(mx-mn)
        return sm  

#Above soln is not optimized 

    def subArrayRanges(self, A0):
        res = 0
        inf = float('inf')
        A = [-inf] + A0 + [-inf]
        s = []
        for i, x in enumerate(A):
            while s and A[s[-1]] > x:
                j = s.pop()
                k = s[-1]
                res -= A[j] * (i - j) * (j - k)
            s.append(i)
            
        A = [inf] + A0 + [inf]
        s = []
        for i, x in enumerate(A):
            while s and A[s[-1]] < x:
                j = s.pop()
                k = s[-1]
                res += A[j] * (i - j) * (j - k)
            s.append(i)
        return res
    
    #Optimized Solution by Lee