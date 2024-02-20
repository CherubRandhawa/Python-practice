def trap(self, height: List[int]) -> int:

        if not height: return 0

        l, r = 0, len(height) - 1
        leftmax = height[l]
        rightmax = height[r]
        res = 0

        while l < r:
            if leftmax < rightmax:                  #coz we working on min(leftmax, rightmax)
                l += 1
                leftmax = max(leftmax, height[l])
                res += leftmax - height[l]
            else:
                r -= 1
                rightmax = max(rightmax, height[r])
                res += rightmax - height[r]
        
        return res