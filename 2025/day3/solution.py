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
            


        
            

if __name__ == "__main__":
    path = './input.txt'
    input_lines = process_input(path)
    result = part1(input_lines)
    print(f'Result: {result}')