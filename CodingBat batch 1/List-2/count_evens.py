def count_evens(nums):
    return sum(1 for i in nums if i % 2 == 0)