def centered_average(nums):
    return int(sum(sorted(nums)[1:-1]) / (len(nums)-2))