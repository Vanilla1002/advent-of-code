def process_input(file_path):
    output = []
    with open (file_path) as file:
        for line in file.readlines():
            output.append([ch for ch in line.strip()])

    return output

def part1(list1 :list[list[str]]) -> int:
    result = 0 
    lasers = set()
    for i, j in enumerate(list1[0]):
        if j =="S":
            lasers.add(i)
            break
    for row in list1[1:]:
        helper_laser= []
        lasers_to_remove = []
        for laser in lasers:
            if row[laser] == '^':
                result +=1
                helper_laser.append(laser - 1)
                helper_laser.append(laser + 1)
                lasers_to_remove.append(laser)
        lasers.update(helper_laser)
        lasers.difference_update(lasers_to_remove)
    return result
def part2(list2 :list[list[str]]):
    result = 0 
    for i, j in enumerate(list2[0]):
        if j =="S":
            list2[0][i] = 1
            break
    for r in range(len(list2)):
        for c in range(len(list2[0])):
            if not isinstance(list2[r][c], int):
                continue
            current_val = list2[r][c]
            next_r = r + 1
            if next_r >= len(list2):
                result += current_val
                continue
            next_cell = list2[next_r][c]
            if next_cell == '^':
                if c -1 >=0:
                    try:
                        list2[next_r][c -1] += current_val
                    except TypeError:
                        list2[next_r][c -1] = current_val
                if c +1 < len(list2[0]):
                    try:
                        list2[next_r][c +1] += current_val
                    except TypeError:
                        list2[next_r][c +1] = current_val
            else:
                try:
                    list2[next_r][c] += current_val
                except TypeError:
                    list2[next_r][c] = current_val
    return result
if __name__ == "__main__":
    path = './input.txt'
    input_lines = process_input(path)
    result = part1(input_lines)
    print(f'Result: {result}')
    result2 = part2(input_lines)
    print(f'Result part 2: {result2}')
