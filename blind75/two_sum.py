nums = [1, 2, 3, 7]
target = 9

num_dict = {}

for i in range(len(nums)):
    find = target - nums[i]
    if find in num_dict:
        print(num_dict[find], i)
    else:
        num_dict[nums[i]] = i
