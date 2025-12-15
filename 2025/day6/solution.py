import re

def process_input(path: str) -> list[list[object]]:
    with open(path, 'r') as f:
        result: list[list[object]] = []
        for line in f.read().splitlines():
            # Find tokens: numbers (contiguous digits) or any non-space, non-digit symbol
            raw_tokens = re.findall(r"\d+|[^\s\d]", line)
            tokens: list[object] = [int(t) if t.isdigit() else t for t in raw_tokens]
            result.append(tokens)
        return result

def part1(input_data: list[list[object]]) -> int:
    result = 0
    for i, j in enumerate(input_data[-1]):
        if j == '*':
            helper = 1
            for k in range(len(input_data)-1):
                if isinstance(input_data[k][i], int):
                    helper *= input_data[k][i]
            result += helper
        elif j == '+':
            helper = 0
            for k in range(len(input_data)-1): 
                if isinstance(input_data[k][i], int):
                    helper += input_data[k][i]
            result += helper
    return result



if __name__ == "__main__":
    path = './input.txt'
    input_lines = process_input(path)
    result = part1(input_lines)
    print(f'Result: {result}')
