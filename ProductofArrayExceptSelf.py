def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))  # Initialize the result array with all elements set to 1.
        prefix = 1  # Initialize a variable to keep track of the product of elements before the current index.

        # Calculate the prefix products and store them in the result array.
        for i in range(len(nums)):
            res[i] = prefix  # Store the product of elements before the current index in the result array.
            prefix *= nums[i]  # Update the prefix product for the next iteration.

        postfix = 1  # Initialize a variable to keep track of the product of elements after the current index.

        # Calculate the postfix products and update the result array.
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix  # Update the result array by multiplying the postfix product.
            postfix *= nums[i]  # Update the postfix product for the next iteration.

        return res  # Return the final result array.
