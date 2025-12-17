def process_input(path: str) -> list[str]:
    with open(path, 'r') as f:
        lines = f.read().splitlines()
        result: list[tuple[int, int]] = []
        for line in lines:
            a,b = line.split(',')
            result.append((int(a), int(b)))
    return result

def part1(input_data: list[tuple[int, int]]) -> int:
    result = 0
    sorted_data = sorted(input_data, key=lambda pair: (pair[1], pair[0]))
    for i in range(len(sorted_data)):
        for j in range(i):
            d = abs(sorted_data[i][1] - sorted_data[j][1] + 1) * abs(sorted_data[i][0] - sorted_data[j][0]+ 1)
            if d > result:
                result = d

    return result
if __name__ == "__main__":
    path = './input.txt'
    input_lines = process_input(path)
    result = part1(input_lines)
    print(f'Result: {result}')