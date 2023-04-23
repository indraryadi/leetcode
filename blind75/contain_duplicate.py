# nums = [1,2,3,4,5]
# nums = [1,2,3,1,5]
# nums = [1,1,1,2,3,4,5]
nums = [1, 4, 1, 5]

# list vs set
# difference time complexity when itterate and search using in operator is
# list = O(n)
# set = O(1)
nums_set = set()


def check_duplicate(nums):
    for i in nums:
        if i in nums_set:
            return True
        else:
            nums_set.add(i)
    return False


print(check_duplicate(nums))
print(nums_set)
