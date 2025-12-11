from part1 import part2_list
from part1 import result as part1_result
from part1 import is_safe

result = 0


def is_safe2(list_of_nums: list):
    
    for idx in range(len(list_of_nums)):
        helper_list = list_of_nums[:idx] + list_of_nums[idx + 1:]
        if is_safe(helper_list):
            return True
    
    return False

for i in part2_list:
    is_increasing = i[0] < i[1]
    if is_safe2(i):
        
        result += 1

print(part1_result)
print(result + part1_result)


