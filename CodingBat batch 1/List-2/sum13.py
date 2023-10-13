def sum13(nums):
    return sum([nums[i] for i in range(len(nums)) if nums[i] != 13 and (i == 0 or nums[i-1] != 13)])