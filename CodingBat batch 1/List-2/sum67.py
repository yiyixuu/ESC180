def sum67(nums):
    if len(nums) == 0:
        return 0
    else:
        while 6 in nums:
            six = nums.index(6)
            seven = nums.index(7, six)
            nums = nums[:six] + nums[seven + 1:]
        return sum(nums)