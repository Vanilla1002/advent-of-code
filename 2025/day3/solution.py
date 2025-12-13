from collections import deque
def process_input(file_path):
    output = []
    with open (file_path) as file:
        for line in file.readlines():
            output.append(line.strip())
    return output

def part1 (list1 :list[str]) -> int:
    result = 0
    for bank in list1:
        pointer1 = 0
        pointer2 = 0
        for i in range(1, len(bank)-1):
            int_i = int(bank[i])
            if int_i > pointer1:
                pointer1 = int_i
                pointer2=0
            elif int_i > pointer2:
                pointer2 = int_i
        if pointer2 < int(bank[-1]):
            pointer2 = int(bank[-1])
        result += pointer1 * 10 + pointer2

    return result

def helper_function(count_positions: dict[int, deque[int]], n: int, length: int) -> int:
    result =[]
    current_index = -1
    while len(result)<n:
        found_change = False
        l_result = len(result)
        for key in sorted(count_positions.keys(), reverse=True):
            while count_positions[key] and count_positions[key][0] <= current_index:
                count_positions[key].popleft()
            if not count_positions[key]:
                continue
            if (n - l_result)> length-count_positions[key][0]:
                continue
            
            current_index = count_positions[key].popleft()
            result.append(key)
            found_change = True
            break
        if not found_change:
            break
    def caclulate_score(res: list[int]) -> int:
        score = 0
        for index, val in enumerate(res):
            score += val * (10 ** (n - index - 1))
        return score
    return caclulate_score(result)


            
def part2 (list1 :list[str], n :int) -> int:
    result = 0 

    for bank in list1:
        count_positions = {}
        l = len(bank)
        for i in range(l):
            int_i = int(bank[i])
            if int_i not in count_positions:
                count_positions[int_i] = deque()
            count_positions[int_i].append(i)
        result += helper_function(count_positions, n, l)
    return result



        
            

if __name__ == "__main__":
    path = './input.txt'
    input_lines = process_input(path)
    result = part1(input_lines)
    result2 = part2(input_lines, 12)
    print(f'Result: {result}')
    print(f'Result 2: {result2}')