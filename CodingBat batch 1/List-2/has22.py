def has22(nums): 
    return max([nums[i]==2 and nums[i+1]==2 for i in range(len(nums)-1)] + [False])