class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        
        A = [-math.inf] + A + [-math.inf]
        n = len(A)
        
        st = []
        res = 0
        
        for i in range(n):
            
            while st and A[st[-1]] > A[i]: # monotonic increasing stack
                mid = st.pop()
                left = st[-1] # previous smaller element
                right = i #next smaller element
                
                res += A[mid] * (mid - left) * (right - mid)
            
            st.append(i)
        return res %(10**9 + 7)
    
#Can also be done by brute force but above soln is using monotonin stack and hiistogram emthod.