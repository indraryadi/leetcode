# nums = [1,2,3,4,5]
#nums = [1,2,3,1,5]
#nums = [1,1,1,2,3,4,5]
nums = [1,4,1,5]

nums_list = [] 

def check_duplicate(nums):
    for i in nums:
        if i in nums_list:
            return True
        else:
            nums_list.append(i) 
    return False

print(check_duplicate(nums))
print(nums_list)
