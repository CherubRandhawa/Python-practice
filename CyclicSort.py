##################CYCLIC SORT##################################

def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        correct_position = nums[i] - 1  # The correct position for the current element
        if nums[i] != nums[correct_position]:
            nums[i], nums[correct_position] = nums[correct_position], nums[i]
        else:
            i += 1