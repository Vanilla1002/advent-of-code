result = 0
part2_list = []
def is_safe(list_of_nums: list):
    if list_of_nums[0]< list_of_nums[1]:
        is_increasing = True
    else:
        is_increasing = False
    for i in range(len(list_of_nums) - 1):
        
        diff = list_of_nums[i+1] - list_of_nums[i]
        if is_increasing and diff not in (1, 2, 3):
            return False
        if not is_increasing and diff not in (-1, -2, -3):
            return False
    return True


with open ('.\day2\input2.txt') as f:
    for line in f :
        is_increasing = False
        list_of_nums = [int(i) for i in line.split()]

        if list_of_nums[0]< list_of_nums[1]:
            is_increasing = True
        if is_safe(list_of_nums):
            result += 1
        else:
            part2_list.append(list_of_nums)
# print(part2_list)
# print(result)


