def recursive_function(nums, target_sum, current_sum=0, index=1):
    if index == len(nums):
        return current_sum == target_sum

    next_num = nums[index]
    return (
        recursive_function(nums, target_sum, current_sum + next_num, index + 1) or
        recursive_function(nums, target_sum, current_sum * next_num, index + 1)
    )

def concatenate_numbers(num1, num2):
    return int(f"{num1}{num2}")

def recursive_function2(nums, target_sum, current_sum=0, index=1):
    if index == len(nums):
        return current_sum == target_sum

    next_num = nums[index]
    return (
        recursive_function2(nums, target_sum, current_sum + next_num, index + 1) or
        recursive_function2(nums, target_sum, current_sum * next_num, index + 1) or
        recursive_function2(nums, target_sum, concatenate_numbers(current_sum, next_num), index + 1)
    )

def process_input(file_path):
    result1, result2 = 0, 0

    with open(file_path) as file:
        for line in file:
            parts = line.split()
            target_sum = int(parts[0][:-1])
            nums = [int(num) for num in parts[1:]]

            if recursive_function(nums, target_sum, nums[0]):
                result1 += target_sum

            if recursive_function2(nums, target_sum, nums[0]):
                result2 += target_sum

    return result1, result2

if __name__ == "__main__":
    input_file = './day7/input7.txt'
    result1, result2 = process_input(input_file)
    print(result1, result2)
