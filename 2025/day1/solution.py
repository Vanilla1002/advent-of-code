
def process_input(file_path):
    output = []
    with open (file_path) as file:
        for line in file.readlines():
            output.append(line.strip())
    return output

def input_praser(line :str) -> int:
    if line[0] == 'L':
        return -int(line[1:])
    else:
        return int(line[1:])

def part1(list1 :list[str]) -> int:
    current = 50
    result = 0
    for i in list1:
        step = input_praser(i)
        current = (current + step) % 100
        print(current)
        if current == 0:
            result += 1
    return result
            
def part2(list1 :list[str]) -> int:
    current = 50
    result = 0
    for i in list1:
        step = input_praser(i)
        helper = (step + current) // 100 
        if (current == 0 and step < 0 and step % 100 != 0):
            result -= 1
        if (step < 0 and (current + step) % 100 == 0):
            result += 1
        current = (current + step) % 100
        result += abs(helper)

    return result

    

    

    


if __name__ == "__main__":
    path = './input.txt'
    input_lines = process_input(path)
    result = part1(input_lines)

    #print(f'Result: {result}')
    result2 = part2(input_lines)
    print(f'Result part 2: {result2}')