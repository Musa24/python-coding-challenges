# Solution one (0(n^2))
# def count_sum(nums,k):
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i] + nums[j] == 17:
#                 return True
#     return False


# Solution one (0(n))
def count_sum(nums,k):
    for num in nums:
        if k-num in nums:
            return True
    return False

print(count_sum([],10))            # False
print(count_sum([10,15,3,7],17))   # True
print(count_sum([11,10,2,5,6],9))  # False
