def find_all_pair(nums,sum):
    flag = True
    for i in range(len(nums)):
        diff = sum - nums[i]
        if diff in nums[i+1:]:
            print(nums[i],diff)
            flag = False
    if flag:
            print("No pair Found")
        

nums = [8,7,2,5,3,1]
sum =  10
find_all_pair(nums,sum) # (8,3)