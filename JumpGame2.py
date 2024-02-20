class Solution:
    def jump(self, nums: List[int]) -> int:
        # Get the length of the input array
        n = len(nums)
        
        # Check if the array has only one element (already at the last index)
        if n == 1:
            return 0  # No jumps needed, already at the last index

        # Initialize variables to keep track of jumps and reachable indices
        jumps = 0           # Number of jumps needed
        current_end = 0     # The maximum index reachable with the current number of jumps
        farthest = 0        # The maximum index reachable with the next jump

        # Iterate through the array (up to the second-to-last element)
        for i in range(n - 1):
            # Update farthest reachable index with the next jump
            farthest = max(farthest, i + nums[i])

            # Check if the current index reaches the maximum reachable index with the current jumps
            if i == current_end:
                # Increment jumps, as a jump is needed to continue further
                jumps += 1
                # Update current_end to the farthest reachable index with the next jump
                current_end = farthest

        # Return the total number of jumps needed to reach the last index
        return jumps
